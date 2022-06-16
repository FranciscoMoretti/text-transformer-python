from patterns import Pattern, PatternList

SEPARATOR_LIST_SAMPLE = PatternList(
    [
        Pattern(name="foo", value="foo_value"),
        Pattern(name="bar", value="bar_value"),
    ]
)


def test_get_values():
    assert SEPARATOR_LIST_SAMPLE.get_values() == ["foo_value", "bar_value"]
