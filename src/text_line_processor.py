import re
from typing import Callable, List, Optional, Union

from src.matching import Matching
from src.named_patterns import NamedPattern
from src.pattern_registry import PatternRegistry
from src.text_line import TextLine

RegexReplacement = Union[str, Callable[[re.Match], str]]


class TextLineProcessor:
    def __init__(self, text_line: TextLine) -> None:
        self.text_line = text_line

    def search_matchings_of_patterns(
        self, pattern_registry: PatternRegistry
    ) -> List[Matching]:
        line_matchings: List[Matching] = []
        for pattern in pattern_registry.patterns:
            if matching := self.search_matching_of_pattern(pattern):
                line_matchings.append(matching)
        return line_matchings

    def search_matching_of_pattern(
        self, pattern: NamedPattern
    ) -> Optional[Matching]:
        if match := pattern.regex.search(self.text_line.text):
            return Matching(
                pattern_name=pattern.name,
                line_number=self.text_line.line_number,
                match=match,
            )
        return None

    def substitute_pattern_with_replacement(
        self,
        pattern: NamedPattern,
        replacement: RegexReplacement,
    ) -> None:
        self.text_line.text = pattern.regex.sub(
            repl=replacement, string=self.text_line.text
        )
