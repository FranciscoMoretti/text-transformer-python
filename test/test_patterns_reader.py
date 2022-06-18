import json
from pathlib import Path
from patterns_reader import PatternsReader
from test.utils.tmp_path import _get_tmp_path_to_file

from named_patterns import NamedPattern, NamedPatternList


PATTERN_LIST_DICT_SAMPLE = [
    {
        "name": "foo",
        "value": "foo_value",
    },
    {
        "name": "bar",
        "value": "bar_value",
    },
]

PATTERN_LIST_SAMPLE = NamedPatternList(
    [
        NamedPattern(name="foo", value="foo_value"),
        NamedPattern(name="bar", value="bar_value"),
    ]
)


def test_from_dict():
    assert PATTERN_LIST_SAMPLE == PatternsReader.from_list_of_dictionaries(
        PATTERN_LIST_DICT_SAMPLE
    )


def test_from_json(tmp_path):
    filepath = _get_tmp_path_to_file(tmp_path)
    filepath.write_text(json.dumps(PATTERN_LIST_DICT_SAMPLE))
    assert PATTERN_LIST_SAMPLE == PatternsReader.from_json_file(filepath)


PATH_TO_PATTERNS_SAMPLE_FILE = Path("./test/patterns_sample.json")


def test_read_from_file():
    expected_list = NamedPatternList([NamedPattern(name="foo", value='foo="bar"')])
    assert expected_list == PatternsReader.from_json_file(PATH_TO_PATTERNS_SAMPLE_FILE)
