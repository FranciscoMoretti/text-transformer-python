import json
from pathlib import Path
from test.utils.tmp_path import _get_tmp_path_to_file

from src.patterns_reader import PatternsReader
from src.search_configuration import SearchConfiguration

PATTERN_LIST_DICT_SAMPLE = [
    {
        "name": "foo",
        "regex_pattern": "foo_value",
    },
    {
        "name": "bar",
        "regex_pattern": "bar_value",
    },
]

PATTERN_LIST_SAMPLE = [
    SearchConfiguration(name="foo", regex_pattern="foo_value"),
    SearchConfiguration(name="bar", regex_pattern="bar_value"),
]


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
    expected_list = [
        SearchConfiguration(name="foo", regex_pattern='foo="bar"')
    ]
    assert expected_list == PatternsReader.from_json_file(
        PATH_TO_PATTERNS_SAMPLE_FILE
    )
