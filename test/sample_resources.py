from src.search_configuration import (
    SearchConfiguration,
    SearchConfigurationList,
)

PATTERNS_SAMPLE = [
    {"regex_pattern": "foo_value", "name": "foo"},
    {"regex_pattern": "bar_value", "name": "bar"},
]

PATTERN_LIST_SAMPLE = SearchConfigurationList(
    [
        SearchConfiguration(
            name=pattern["name"], regex_pattern=pattern["regex_pattern"]
        )
        for pattern in PATTERNS_SAMPLE
    ]
)
