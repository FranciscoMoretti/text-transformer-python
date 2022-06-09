from separators import Separator, SeparatorList


def test_get_values():
    assert SeparatorList(
        [
            Separator(name="foo", value="foo_value"),
            Separator(name="bar", value="bar_value"),
        ]
    ).get_values() == ["foo_value", "bar_value"]
