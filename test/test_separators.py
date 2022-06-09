import json
from separators import Separator, SeparatorList
from test.utils.tmp_path import _get_tmp_path_to_file


SEPARATOR_LIST_SAMPLE = SeparatorList(
    [
        Separator(name="foo", value="foo_value"),
        Separator(name="bar", value="bar_value"),
    ]
)

SEPARATOR_LIST_DICT_SAMPLE = [
    {
        "name": "foo",
        "value": "foo_value",
    },
    {
        "name": "bar",
        "value": "bar_value",
    },
]


def test_get_values():
    assert SEPARATOR_LIST_SAMPLE.get_values() == ["foo_value", "bar_value"]


def test_from_dict():
    assert SEPARATOR_LIST_SAMPLE == SeparatorList.from_list_of_dictionaries(
        SEPARATOR_LIST_DICT_SAMPLE
    )


def test_from_json(tmp_path):
    filepath = _get_tmp_path_to_file(tmp_path)
    filepath.write_text(json.dumps(SEPARATOR_LIST_DICT_SAMPLE))
    assert SEPARATOR_LIST_SAMPLE == SeparatorList.from_json_file(filepath)
