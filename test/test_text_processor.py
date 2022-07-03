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
    matchings = file_processor.search_matchings_of_pattern(pattern=test_input)
    assert matchings == expected
