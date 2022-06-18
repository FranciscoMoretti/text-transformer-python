from pathlib import Path
from typing import List, Optional, OrderedDict
from matching import Matching
from named_patterns import NamedPatternList
from pattern_registry import PatternRegistry
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
        self, separators: PatternRegistry
    ) -> List[VirtualFile]:
        lines_of_separators = self.get_matched_lines_by_patterns(patterns=separators)

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

    def get_matched_lines_by_patterns(
        self, patterns: PatternRegistry
    ) -> OrderedDict[str, List[TextLine]]:
        matchings = self.get_line_matchings_of_patterns(patterns)
        lines_by_pattern: OrderedDict[str, List[TextLine]] = OrderedDict(
            {pattern_name: [] for pattern_name in patterns.get_pattern_names()}
        )
        for matching in matchings:
            lines_by_pattern[matching.pattern_name].append(
                TextLine(text=matching.match.string, line_number=matching.line_number)
            )
        return lines_by_pattern

    def get_line_matchings_of_patterns(
        self,
        patterns: PatternRegistry,
    ) -> List[Matching]:
        line_matchings: List[Matching] = []
        for text_line in self.virtual_file.get_text_lines():
            line_matchings.extend(
                patterns.search_matchings_in_text_line(text_line=text_line)
            )
        return line_matchings
