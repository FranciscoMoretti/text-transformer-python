from src.named_patterns import SearchConfiguration
from src.text_processor import TextProcessor

MULTILINE_CONTENT = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\n"


def test_search_matchings_of_pattern():
    file_processor = TextProcessor(MULTILINE_CONTENT)
    pattern = SearchConfiguration(name="bar", regex_pattern="Line 3")

    matchings = file_processor.search_matchings_of_pattern(pattern=pattern)
    assert len(matchings) == 1
    assert MULTILINE_CONTENT[matchings[0].start : matchings[0].end] == "Line 3"
