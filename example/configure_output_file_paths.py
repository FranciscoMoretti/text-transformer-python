from pathlib import Path
from typing import List

from src.text_file import TextFile


def configure_output_file_paths(
    files: List[TextFile], prefix_path: Path, file_suffix: str
) -> List[TextFile]:
    for file in files:
        file.path = Path.joinpath(prefix_path, file.path).with_suffix(
            file_suffix
        )
    return files
