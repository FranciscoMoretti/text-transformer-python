from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
from separators import Separator, SeparatorList
from text_line import TextLine

from virtual_file import VirtualFile


class VirtualFileProcessor:
    def __init__(self, virtual_file: VirtualFile) -> None:
        self.virtual_file = virtual_file

    def get_text_lines_that_match_separators(
        self, separators: SeparatorList
    ) -> Dict[str, List[TextLine]]:
        return self._get_lines_that_contains_patterns(separators)

    def _get_lines_that_contains_patterns(
        self,
        named_patterns: SeparatorList,
    ) -> Dict[str, List[TextLine]]:
        lines_by_match_pattern: Dict[str, List[TextLine]] = {
            match_pattern: [] for match_pattern in named_patterns
        }
        for line_number, line_text in enumerate(self.virtual_file.lines):
            for match_pattern in named_patterns:
                if match_pattern.value in line_text:
                    lines_by_match_pattern[match_pattern.name].append(
                        TextLine(text=line_text, line_number=line_number)
                    )
        return lines_by_match_pattern
