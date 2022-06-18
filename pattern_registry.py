from typing import List

from matching import Matching
from named_patterns import NamedPatternList
from text_line import TextLine


class PatternRegistry:
    def __init__(self, patterns: NamedPatternList) -> None:
        self.patterns = patterns

    def search_matchings_in_text_line(self, text_line: TextLine) -> List[Matching]:
        line_matchings: List[Matching] = []
        for pattern in self.patterns:
            if match := pattern.regex.search(text_line.text):
                line_matchings.append(
                    Matching(
                        pattern_name=pattern.name,
                        line_number=text_line.line_number,
                        match=match,
                    )
                )
        return line_matchings

    def get_pattern_names(self) -> List[str]:
        return [pattern.name for pattern in self.patterns]
