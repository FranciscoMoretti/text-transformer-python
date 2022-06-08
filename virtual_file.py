from argparse import ArgumentError
from dataclasses import dataclass
from pathlib import Path
from typing import  Optional

@dataclass
class VirtualFile:
    lines: str
    path: Optional[Path] = None

class VirtualFileIO:
    @staticmethod
    def read_from_path(filepath: Path) -> VirtualFile:
        with open(filepath) as open_file:
            return VirtualFile(
                lines=open_file.readlines(),
                path=filepath
            )

    @staticmethod
    def save_to_real_file(virtual_file: VirtualFile):
        if virtual_file.path is None:
            raise ArgumentError(message="Virtual file must have a file path to be saved on a real file.")

        with open(virtual_file.path, "w") as open_file:
            open_file.writelines(virtual_file.lines)
  
