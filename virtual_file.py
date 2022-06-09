from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class VirtualFile:
    lines: List[str]
    path: Path


class VirtualFileIO:
    @staticmethod
    def read_from_path(filepath: Path) -> VirtualFile:
        with open(filepath, encoding="UTF-8") as open_file:
            return VirtualFile(lines=open_file.readlines(), path=filepath)

    @staticmethod
    def save_to_real_file(virtual_file: VirtualFile):
        with open(virtual_file.path, "w", encoding="UTF-8") as open_file:
            open_file.writelines(virtual_file.lines)
