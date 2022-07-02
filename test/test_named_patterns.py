import re
from test.sample_resources import PATTERN_LIST_SAMPLE, PATTERNS_SAMPLE


def test_get_values():
    assert PATTERN_LIST_SAMPLE.get_patterns() == [
        pattern["regex_pattern"] for pattern in PATTERNS_SAMPLE
    ]


def test_get_regexps():
    assert PATTERN_LIST_SAMPLE.get_regexps() == [
        re.compile(pattern["regex_pattern"]) for pattern in PATTERNS_SAMPLE
    ]
