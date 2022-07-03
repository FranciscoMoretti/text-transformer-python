from typing import List

from src.matching import SimpleMatching
from src.named_patterns import SearchConfiguration
from src.text_line_processor import RegexReplacement


class TextProcessor:
    def __init__(self, text: str) -> None:
        self._text = text

    def search_matchings_of_pattern(
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
