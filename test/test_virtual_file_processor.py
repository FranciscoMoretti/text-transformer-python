from pathlib import Path
from virtual_file import VirtualFile
from virtual_file_processor import VirtualFileProcessor

MULTILINE_CONTENT = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n"]
VIRTUAL_FILE = VirtualFile(lines=MULTILINE_CONTENT, path=Path())


def test_get_raw_lines_in_range():
    file_processor = VirtualFileProcessor(VIRTUAL_FILE)
    assert file_processor.get_raw_lines_in_range(end_line=2) == MULTILINE_CONTENT[:2]
    assert file_processor.get_raw_lines_in_range(start_line=2) == MULTILINE_CONTENT[2:]
    assert (
        file_processor.get_raw_lines_in_range(start_line=1, end_line=2)
        == MULTILINE_CONTENT[1:2]
    )
