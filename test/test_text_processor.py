import pytest

from src.matching import SimpleMatching
from src.named_patterns import SearchConfiguration
from src.text_processor import TextProcessor

MULTILINE_CONTENT = (
    "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7"
    '\n## <a name="SS-aims"></a>In.aims: Aims'
)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            SearchConfiguration(name="bar", regex_pattern="Line 3"),
            [SimpleMatching(pattern_name="bar", start=14, end=20)],
            id="simple_pattern_found",
        ),
        pytest.param(
            SearchConfiguration(
                name="bar", regex_pattern=r'.*name="(?P<bar>[A-Za-z0-9-]*)".*'
            ),
            [SimpleMatching(pattern_name="bar", start=49, end=87)],
            id="regex_pattern_found",
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
    ],
)
def test_split_at_positions(positions, expected):
    text_processor = TextProcessor(MULTILINE_CONTENT)
    new_text = text_processor.split_at_positions(positions)
    assert new_text == expected


def test_get_line_iterator():
    text_processor = TextProcessor(MULTILINE_CONTENT)
    line_iterator = text_processor.get_line_iterator()
    assert list(line_iterator) == MULTILINE_CONTENT.splitlines()
