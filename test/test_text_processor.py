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
    "search_configuration, expected",
    [
        pytest.param(
            SearchConfiguration(name="bar", regex_pattern=r"Line 3\n"),
            MULTILINE_CONTENT.split("Line 3\n"),
            id="split_by_one_line",
        ),
    ],
)
def test_split_with_pattern(search_configuration, expected):
    text_processor = TextProcessor(MULTILINE_CONTENT)
    new_text = text_processor.split_with_pattern(pattern=search_configuration)
    assert new_text == expected
