from src.named_patterns import SearchConfiguration, SearchConfigurationList
from src.pattern_registry import PatternRegistry

PATTERNS = [
    {"regex_pattern": "foo_value", "name": "foo"},
    {"regex_pattern": "bar_value", "name": "bar"},
]

SEPARATOR_LIST_SAMPLE = SearchConfigurationList(
    [
        SearchConfiguration(
            name=pattern["name"], regex_pattern=pattern["regex_pattern"]
        )
        for pattern in PATTERNS
    ]
)


def test_patterns_registry_construction():
    patterns_registry = PatternRegistry(patterns=SEPARATOR_LIST_SAMPLE)
    assert isinstance(patterns_registry, PatternRegistry)
