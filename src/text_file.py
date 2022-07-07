from dataclasses import dataclass
from pathlib import Path


@dataclass
class TextFile:
    text: str
    path: Path
