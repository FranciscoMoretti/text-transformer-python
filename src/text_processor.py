from typing import Generator, List, Optional

from src.itertools_recipes import pairwise
from src.line_iterator import line_iterator
from src.matching import SimpleMatching
from src.regex_types import RegexReplacement
from src.search_configuration import SearchConfiguration


class TextProcessor:
    def __init__(self, text: str) -> None:
        self._text = text

    def get_text(self) -> str:
        return self._text

    def find_matchings_of_pattern(
        self,
        pattern: SearchConfiguration,
    ) -> List[SimpleMatching]:
        return [
            SimpleMatching(
                text=self._text[match.start() : match.end()],
                pattern_name=pattern.name,
                start=match.start(),
                end=match.end(),
            )
            for match in pattern.regex.finditer(self._text)
        ]

    def substitute_pattern_with_replacement(
        self, pattern: SearchConfiguration, replacement: RegexReplacement
    ):
        self._text = pattern.regex.sub(repl=replacement, string=self._text)

    def split_at_pattern(self, pattern: SearchConfiguration) -> List[str]:
        return pattern.regex.split(string=self._text)

    def split_at_positions(self, positions: List[int]) -> List[str]:
        sorted_positions = sorted(positions)
        start_limit = [0] if next(iter(sorted_positions), None) != 0 else []
        last_postion = len(self._text) + 1
        end_limit = (
            [last_postion]
            if next(reversed(sorted_positions), None) != last_postion
            else []
        )
        positions_with_limits = start_limit + sorted_positions + end_limit
        return [
            self._text[start:end]
            for start, end in pairwise(positions_with_limits)
        ]

    def get_line_iterator(self) -> Generator[str, None, None]:
        return line_iterator(raw_string=self._text)

    def get_text_in_line_range(
        self, start: Optional[int] = None, end: Optional[int] = None
    ) -> str:
        lines = list(line_iterator(raw_string=self._text))
        start = 0 if start is None else start
        end = len(lines) if end is None else end
        return "\n".join(lines[start:end])
