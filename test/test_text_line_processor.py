from src.named_patterns import NamedPattern, NamedPatternList
from src.pattern_registry import PatternRegistry
from src.text_line import TextLine
from src.text_line_processor import TextLineProcessor

PATTERNS = [
    {"value": "foo_value", "name": "foo"},
    {"value": "bar_value", "name": "bar"},
]

PATTERN_LIST_SAMPLE = NamedPatternList(
    [
        NamedPattern(name=pattern["name"], value=pattern["value"])
        for pattern in PATTERNS
    ]
)


SAMPLE_TEXT_LINE_BAR = "this line has bar_value in it"


def test_search_matching_of_pattern():
    foo_pattern = PATTERN_LIST_SAMPLE[0]
    bar_pattern = PATTERN_LIST_SAMPLE[1]
    text_line = TextLine(text=SAMPLE_TEXT_LINE_BAR, line_number=100)
    text_line_processor = TextLineProcessor(text_line)
    assert text_line_processor.search_matching_of_pattern(foo_pattern) is None
    assert (
        text_line_processor.search_matching_of_pattern(bar_pattern) is not None
    )


def test_search_matchings_of_patterns():
    pattern_registry = PatternRegistry(patterns=PATTERN_LIST_SAMPLE)
    text_line = TextLine(text=SAMPLE_TEXT_LINE_BAR, line_number=100)
    text_line_processor = TextLineProcessor(text_line)
    assert (
        len(text_line_processor.search_matchings_of_patterns(pattern_registry))
        == 1
    )
