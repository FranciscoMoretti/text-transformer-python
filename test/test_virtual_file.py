from virtual_file import VirtualFile, VirtualFileIO

CONTENT = "content"


def test_read_file(tmp_path):
    path = _get_tmp_path_to_file(tmp_path)
    path.write_text(CONTENT)
    assert VirtualFileIO.read_from_path(path) == VirtualFile(lines=[CONTENT], path=path)


def test_save_file(tmp_path):
    path = _get_tmp_path_to_file(tmp_path)
    virtual_file = VirtualFile(lines=[CONTENT], path=path)
    VirtualFileIO.save_to_real_file(virtual_file)
    assert path.read_text() == CONTENT


def _get_tmp_path_to_file(tmp_path):
    directory = tmp_path / "sub"
    directory.mkdir()
    return directory / "foo.txt"
