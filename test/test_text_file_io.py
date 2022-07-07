from test.utils.tmp_path import _get_tmp_path_to_file

from src.text_file import TextFile
from src.text_file_io import TextFileIO

CONTENT = "content"
MULTILINE_CONTENT = "Line 1\nLine 2\nLine 3\n"


def test_read_file(tmp_path):
    path = _get_tmp_path_to_file(tmp_path)
    path.write_text(CONTENT)
    assert TextFileIO.read_from_path(path) == TextFile(text=CONTENT, path=path)


def test_save_file(tmp_path):
    path = _get_tmp_path_to_file(tmp_path)
    virtual_file = TextFile(text=CONTENT, path=path)
    TextFileIO.save_to_real_file(virtual_file)
    assert path.read_text() == CONTENT


def test_save_and_read_multi_line_file(tmp_path):
    path = _get_tmp_path_to_file(tmp_path)
    virtual_file = TextFile(text=MULTILINE_CONTENT, path=path)
    TextFileIO.save_to_real_file(virtual_file)
    assert TextFileIO.read_from_path(path).text == MULTILINE_CONTENT
