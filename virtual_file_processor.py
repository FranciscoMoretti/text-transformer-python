from pathlib import Path
from typing import List, Optional, OrderedDict
from separators import SeparatorList
from text_line import TextLine
from utils import all_items_have_one_item_in_them, pairwise

from virtual_file import VirtualFile


class VirtualFileProcessor:
    def __init__(self, virtual_file: VirtualFile) -> None:
        self.virtual_file = virtual_file

    def get_raw_lines_in_range(
        self,
        start_line: Optional[int] = 0,
        end_line: Optional[int] = None,
    ) -> List[str]:
        if start_line is None:
            start_line = 0
        if end_line is None:
            end_line = len(self.virtual_file.lines) + 1
        return self.virtual_file.lines[start_line:end_line]

    def split_files_with_separators(
        self, separators: SeparatorList
    ) -> List[VirtualFile]:
        lines_of_separators = self.get_text_lines_that_match_separators(
            separators=separators
        )

        # TODO: refactor in order to avoid this hack of adding a fake line
        lines_of_separators["end"] = [
            TextLine(text="", line_number=len(self.virtual_file.lines) + 1)
        ]

        # TODO: this shouldn't be necessary if we use the right types
        assert all_items_have_one_item_in_them(list(lines_of_separators.values()))

        separated_files = []
        for (current_key, current_lines), (_, next_lines) in pairwise(
            lines_of_separators.items()
        ):
            current_separator_name = current_key
            start_line_number = next(iter(current_lines)).line_number
            end_line_number = next(iter(next_lines)).line_number
            virtual_file = VirtualFile(
                path=Path(current_separator_name),
                lines=self.get_raw_lines_in_range(start_line_number, end_line_number),
            )
            separated_files.append(virtual_file)
        return separated_files

    def get_text_lines_that_match_separators(
        self, separators: SeparatorList
    ) -> OrderedDict[str, List[TextLine]]:
        return self._get_lines_that_contains_patterns(separators)

    def _get_lines_that_contains_patterns(
        self,
        named_patterns: SeparatorList,
    ) -> OrderedDict[str, List[TextLine]]:
        lines_by_match_pattern: OrderedDict[str, List[TextLine]] = OrderedDict(
            {match_pattern.name: [] for match_pattern in named_patterns}
        )
        for line_number, line_text in enumerate(self.virtual_file.lines):
            for match_pattern in named_patterns:
                if match_pattern.value in line_text:
                    lines_by_match_pattern[match_pattern.name].append(
                        TextLine(text=line_text, line_number=line_number)
                    )
        return lines_by_match_pattern
