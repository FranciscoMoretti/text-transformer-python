from test.utils.tmp_path import _get_tmp_path_to_file
from virtual_file import VirtualFile, VirtualFileIO

CONTENT = "content"
MULTILINE_CONTENT = ["Line 1\n", "Line 2\n", "Line 3\n"]


def test_read_file(tmp_path):
    path = _get_tmp_path_to_file(tmp_path)
    path.write_text(CONTENT)
    assert VirtualFileIO.read_from_path(path) == VirtualFile(lines=[CONTENT], path=path)


def test_save_file(tmp_path):
    path = _get_tmp_path_to_file(tmp_path)
    virtual_file = VirtualFile(lines=[CONTENT], path=path)
    VirtualFileIO.save_to_real_file(virtual_file)
    assert path.read_text() == CONTENT


def test_save_and_read_multi_line_file(tmp_path):
    path = _get_tmp_path_to_file(tmp_path)
    virtual_file = VirtualFile(lines=MULTILINE_CONTENT, path=path)
    VirtualFileIO.save_to_real_file(virtual_file)
    assert VirtualFileIO.read_from_path(path).lines == MULTILINE_CONTENT
