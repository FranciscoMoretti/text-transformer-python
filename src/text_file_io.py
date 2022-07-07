from pathlib import Path

from src.text_file import TextFile


class TextFileIO:
    @staticmethod
    def read_from_path(filepath: Path) -> TextFile:
        with open(filepath, encoding="UTF-8") as open_file:
            return TextFile(text=open_file.read(), path=filepath)

    @staticmethod
    def save_to_real_file(text_file: TextFile):
        TextFileIO._create_parent_directory(text_file)
        with open(text_file.path, "w", encoding="UTF-8") as open_file:
            open_file.write(text_file.text)

    @staticmethod
    def _create_parent_directory(virtual_file):
        if not virtual_file.path.parent.exists():
            virtual_file.path.parent.mkdir(parents=True, exist_ok=True)
