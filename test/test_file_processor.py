from pathlib import Path

from src.file_processor import FileProcessor
from src.named_patterns import SearchConfiguration
from src.text_file import TextFile
from src.utils import all_items_have_one_item_in_them

MULTILINE_CONTENT = (
    "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7"
    '\n## <a name="SS-aims"></a>In.aims: Aims'
)

TEXT_FILE = TextFile(text=MULTILINE_CONTENT, path=Path())


def test_get_matchings_by_patterns():
    file_processor = FileProcessor(TEXT_FILE)
    patterns = [
        SearchConfiguration(name="foo", regex_pattern="Line 1"),
        SearchConfiguration(name="bar", regex_pattern="Line 3"),
    ]
    matchings_by_patterns = file_processor.get_matchings_by_patterns(
        patterns=patterns
    )
    assert all_items_have_one_item_in_them(
        list(matchings_by_patterns.values())
    )
    assert matchings_by_patterns["foo"][0].text == "Line 1"
    assert matchings_by_patterns["bar"][0].text == "Line 3"


def test_split_files_by_separators():
    file_processor = FileProcessor(TEXT_FILE)
    separators = [
        SearchConfiguration(name="foo", regex_pattern="Line 1\n"),
        SearchConfiguration(name="bar", regex_pattern="Line 3\n"),
        SearchConfiguration(name="baz", regex_pattern="Line 6\n"),
    ]

    output_files = (
        file_processor.split_files_with_separators_starting_and_name(
            separators=separators
        )
    )
    assert len(output_files) == 3
    assert all(isinstance(file, TextFile) for file in output_files)
    assert output_files[1].path == Path("bar")
    assert output_files[1].text == "Line 3\nLine 4\nLine 5\n"
