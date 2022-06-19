from dataclasses import dataclass
from pathlib import Path
from typing import List

from src.text_line import TextLine


@dataclass
class VirtualFile:
    lines: List[str]
    path: Path

    def get_text_lines(self) -> List[TextLine]:
        return [
            TextLine(line_number=number, text=text)
            for number, text in enumerate(self.lines)
        ]


class VirtualFileIO:
    @staticmethod
    def read_from_path(filepath: Path) -> VirtualFile:
        with open(filepath, encoding="UTF-8") as open_file:
            return VirtualFile(lines=open_file.readlines(), path=filepath)

    @staticmethod
    def save_to_real_file(virtual_file: VirtualFile):
        VirtualFileIO._create_parent_directory(virtual_file)
        with open(virtual_file.path, "w", encoding="UTF-8") as open_file:
            open_file.writelines(virtual_file.lines)

    @staticmethod
    def _create_parent_directory(virtual_file):
        if not virtual_file.path.parent.exists():
            virtual_file.path.parent.mkdir(parents=True, exist_ok=True)