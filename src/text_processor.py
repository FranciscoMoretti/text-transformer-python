from typing import List

from src.itertools_recipes import pairwise
from src.matching import SimpleMatching
from src.named_patterns import SearchConfiguration
from src.text_line_processor import RegexReplacement


class TextProcessor:
    def __init__(self, text: str) -> None:
        self._text = text

    def find_matchings_of_pattern(
        self,
        pattern: SearchConfiguration,
    ) -> List[SimpleMatching]:
        return [
            SimpleMatching(
                pattern_name=pattern.name, start=match.start(), end=match.end()
            )
            for match in pattern.regex.finditer(self._text)
        ]

    def substitute_pattern_with_replacement(
        self, pattern: SearchConfiguration, replacement: RegexReplacement
    ) -> str:
        return pattern.regex.sub(repl=replacement, string=self._text)

    def split_at_pattern(self, pattern: SearchConfiguration) -> List[str]:
        return pattern.regex.split(string=self._text)

    def split_at_positions(self, positions: List[int]) -> List[str]:
        positions_with_limits = [0] + positions + [len(self._text) + 1]
        return [
            self._text[start:end]
            for start, end in pairwise(positions_with_limits)
        ]
