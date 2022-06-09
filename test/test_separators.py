from separators import Separator, SeparatorList

SEPARATOR_LIST_SAMPLE = SeparatorList(
    [
        Separator(name="foo", value="foo_value"),
        Separator(name="bar", value="bar_value"),
    ]
)


def test_get_values():
    assert SEPARATOR_LIST_SAMPLE.get_values() == ["foo_value", "bar_value"]
