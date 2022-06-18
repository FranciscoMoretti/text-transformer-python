from named_patterns import NamedPattern, NamedPatternList
from pattern_registry import PatternRegistry

PATTERNS = [
    {"value": "foo_value", "name": "foo"},
    {"value": "bar_value", "name": "bar"},
]

SEPARATOR_LIST_SAMPLE = NamedPatternList(
    [NamedPattern(name=pattern["name"], value=pattern["value"]) for pattern in PATTERNS]
)


def test_patterns_registry_construction():
    patterns_registry = PatternRegistry(patterns=SEPARATOR_LIST_SAMPLE)
    assert isinstance(patterns_registry, PatternRegistry)
