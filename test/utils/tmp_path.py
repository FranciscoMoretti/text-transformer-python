def _get_tmp_path_to_file(tmp_path):
    directory = tmp_path / "sub"
    directory.mkdir()
    return directory / "foo.txt"
