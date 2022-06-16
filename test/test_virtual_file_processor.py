from nis import match
from pathlib import Path
from separators import Separator, SeparatorList
from text_line import TextLine
from utils import all_items_have_one_item_in_them
from virtual_file import VirtualFile
from virtual_file_processor import VirtualFileProcessor

MULTILINE_CONTENT = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n",
    "Line 4\n",
    "Line 5\n",
    "Line 6\n",
    "Line 7\n",
]
VIRTUAL_FILE = VirtualFile(lines=MULTILINE_CONTENT, path=Path())


def test_get_raw_lines_in_range():
    file_processor = VirtualFileProcessor(VIRTUAL_FILE)
    assert file_processor.get_raw_lines_in_range(end_line=2) == MULTILINE_CONTENT[:2]
    assert file_processor.get_raw_lines_in_range(start_line=2) == MULTILINE_CONTENT[2:]
    assert (
        file_processor.get_raw_lines_in_range(start_line=1, end_line=2)
        == MULTILINE_CONTENT[1:2]
    )


def test_get_text_lines_that_match_separators():
    file_processor = VirtualFileProcessor(VIRTUAL_FILE)
    separators = SeparatorList(
        [Separator(name="foo", value="Line 1"), Separator(name="bar", value="Line 3")]
    )
    matched_lines = file_processor.get_text_lines_that_match_separators(
        separators=separators
    )
    assert all_items_have_one_item_in_them(list(matched_lines.values()))
    assert matched_lines["foo"][0] == TextLine(text=MULTILINE_CONTENT[0], line_number=0)
    assert matched_lines["bar"][0] == TextLine(text=MULTILINE_CONTENT[2], line_number=2)
