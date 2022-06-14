from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
from text_line import TextLine

from virtual_file import VirtualFile


class VirtualFileProcessor:
    def __init__(self, virtual_file: VirtualFile) -> None:
        self.virtual_file = virtual_file

    def _find_lines_that_contains_strings(
        self,
        match_patterns: List[str],
    ) -> Dict[str, List[TextLine]]:
        lines_by_match_pattern: Dict[str, List[TextLine]] = {
            match_pattern: [] for match_pattern in match_patterns
        }
        for line_number, line_text in enumerate(self.virtual_file.lines):
            for match_pattern in match_patterns:
                if match_pattern in line_text:
                    lines_by_match_pattern[match_pattern].append(
                        TextLine(text=line_text, line_number=line_number)
                    )
        return lines_by_match_pattern
