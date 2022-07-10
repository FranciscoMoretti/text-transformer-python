from test.sample_resources import MULTILINE_CONTENT

import pytest

from src.matching import SimpleMatching
from src.search_configuration import SearchConfiguration
from src.text_processor import TextProcessor


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            SearchConfiguration(name="bar", regex_pattern="Line 3"),
            [
                SimpleMatching(
                    pattern_name="bar", text="Line 3", start=14, end=20
                )
            ],
            id="simple_pattern_found",
        ),
        pytest.param(
            SearchConfiguration(
                name="bar", regex_pattern=r'.*name="(?P<bar>[A-Za-z0-9-]*)".*'
            ),
            [
                SimpleMatching(
                    pattern_name="bar",
                    text='## <a name="SS-aims"></a>In.aims: Aims',
                    start=49,
                    end=87,
                )
            ],
            id="regex_pattern_found",
        ),
        pytest.param(
            SearchConfiguration(name="bar", regex_pattern=r".*Line 3.*"),
            [
                SimpleMatching(
                    pattern_name="bar",
                    text="Line 3",
                    start=14,
                    end=20,
                )
            ],
            id="regex_one_line_pattern",
        ),
        pytest.param(
            SearchConfiguration(name="bar", regex_pattern=r".*Line [35].*"),
            [
                SimpleMatching(
                    pattern_name="bar",
                    text="Line 3",
                    start=14,
                    end=20,
                ),
                SimpleMatching(
                    pattern_name="bar",
                    text="Line 5",
                    start=28,
                    end=34,
                ),
            ],
            id="regex_one_line_pattern",
        ),
    ],
)
def test_search_matchings_of_pattern(test_input, expected):
    file_processor = TextProcessor(MULTILINE_CONTENT)
    matchings = file_processor.find_matchings_of_pattern(pattern=test_input)
    assert matchings == expected


@pytest.mark.parametrize(
    "search_configuration, replacement, expected",
    [
        pytest.param(
            SearchConfiguration(name="bar", regex_pattern="Line 3"),
            "Line new",
            MULTILINE_CONTENT.replace("Line 3", "Line new"),
            id="simple_replacement",
        ),
        pytest.param(
            SearchConfiguration(name="bar", regex_pattern=".*Line 3.*\n"),
            "",
            MULTILINE_CONTENT.replace("Line 3\n", ""),
            id="line_replacement_with_empty_deletes_line",
        ),
    ],
)
def test_substitute_pattern_with_replacement(
    search_configuration, replacement, expected
):
    text_processor = TextProcessor(MULTILINE_CONTENT)
    new_text = text_processor.substitute_pattern_with_replacement(
        pattern=search_configuration, replacement=replacement
    )
    assert new_text == expected


@pytest.mark.parametrize(
    "positions, expected",
    [
        pytest.param(
            [],
            [MULTILINE_CONTENT],
            id="no_positions_equals_original",
        ),
        pytest.param(
            [10],
            [MULTILINE_CONTENT[:10], MULTILINE_CONTENT[10:]],
            id="start_end_limits_are_used",
        ),
        pytest.param(
            [10, 20, 30],
            [
                MULTILINE_CONTENT[:10],
                MULTILINE_CONTENT[10:20],
                MULTILINE_CONTENT[20:30],
                MULTILINE_CONTENT[30:],
            ],
            id="multi_split_is_allowed",
        ),
        pytest.param(
            [20, 10],
            [
                MULTILINE_CONTENT[:10],
                MULTILINE_CONTENT[10:20],
                MULTILINE_CONTENT[20:],
            ],
            id="positions_order_do_not_matter",
        ),
        pytest.param(
            [0, 10],
            [
                MULTILINE_CONTENT[:10],
                MULTILINE_CONTENT[10:],
            ],
            id="explicit_start_is_allowed",
        ),
        pytest.param(
            [10, len(MULTILINE_CONTENT) + 1],
            [
                MULTILINE_CONTENT[:10],
                MULTILINE_CONTENT[10:],
            ],
            id="explicit_end_is_allowed",
        ),
    ],
)
def test_split_at_positions(positions, expected):
    text_processor = TextProcessor(MULTILINE_CONTENT)
    assert text_processor.split_at_positions(positions) == expected


def test_get_line_iterator():
    text_processor = TextProcessor(MULTILINE_CONTENT)
    assert (
        list(text_processor.get_line_iterator())
        == MULTILINE_CONTENT.splitlines()
    )


@pytest.mark.parametrize(
    "start, end, expected",
    [
        pytest.param(
            None,
            2,
            "\n".join(MULTILINE_CONTENT.splitlines()[:2]),
            id="no_start_defined_starts_at_beggining",
        ),
        pytest.param(
            2,
            None,
            "\n".join(MULTILINE_CONTENT.splitlines()[2:]),
            id="no_end_defined_ends_at_end",
        ),
        pytest.param(
            1,
            3,
            "\n".join(MULTILINE_CONTENT.splitlines()[1:3]),
            id="start_and_end_defined_are_used_as_limits",
        ),
    ],
)
def test_get_text_in_line_range(start, end, expected):
    text_processor = TextProcessor(MULTILINE_CONTENT)
    assert (
        text_processor.get_text_in_line_range(start=start, end=end) == expected
    )
    assert expected in MULTILINE_CONTENT
