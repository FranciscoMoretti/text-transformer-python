import re
from patterns import NamedPattern, NamedPatternList

PATTERNS = [
    {"value": "foo_value", "name": "foo"},
    {"value": "bar_value", "name": "bar"},
]

SEPARATOR_LIST_SAMPLE = NamedPatternList(
    [NamedPattern(name=pattern["name"], value=pattern["value"]) for pattern in PATTERNS]
)


def test_get_values():
    assert SEPARATOR_LIST_SAMPLE.get_patterns() == [
        pattern["value"] for pattern in PATTERNS
    ]


def test_get_regexps():
    assert SEPARATOR_LIST_SAMPLE.get_regexps() == [
        re.compile(pattern["value"]) for pattern in PATTERNS
    ]
