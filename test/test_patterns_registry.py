from src.named_patterns import NamedPattern, NamedPatternList
from src.pattern_registry import PatternRegistry
from src.text_line import TextLine

PATTERNS = [
    {"value": "foo_value", "name": "foo"},
    {"value": "bar_value", "name": "bar"},
]

SEPARATOR_LIST_SAMPLE = NamedPatternList(
    [
        NamedPattern(name=pattern["name"], value=pattern["value"])
        for pattern in PATTERNS
    ]
)


def test_patterns_registry_construction():
    patterns_registry = PatternRegistry(patterns=SEPARATOR_LIST_SAMPLE)
    assert isinstance(patterns_registry, PatternRegistry)


def test_search_matchings_in_text_line():
    patterns_registry = PatternRegistry(patterns=SEPARATOR_LIST_SAMPLE)
    text_line = TextLine(text="this line has bar_value in it", line_number=100)
    assert (
        len(
            patterns_registry.search_matchings_in_text_line(
                text_line=text_line
            )
        )
        == 1
    )
