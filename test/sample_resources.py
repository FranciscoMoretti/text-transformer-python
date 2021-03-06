from src.search_configuration import SearchConfiguration

MULTILINE_CONTENT = """Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
## <a name="SS-aims"></a>In.aims: Aims
"""

PATTERNS_SAMPLE = [
    {"regex_pattern": "foo_value", "name": "foo"},
    {"regex_pattern": "bar_value", "name": "bar"},
]

PATTERN_LIST_SAMPLE = [
    SearchConfiguration(
        name=pattern["name"], regex_pattern=pattern["regex_pattern"]
    )
    for pattern in PATTERNS_SAMPLE
]
