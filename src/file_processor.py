from pathlib import Path
from typing import Dict, List

from src.matching import SimpleMatching
from src.named_patterns import SearchConfiguration
from src.text_file import TextFile
from src.text_processor import TextProcessor


class FileProcessor:
    def __init__(self, text_file: TextFile) -> None:
        self._text_file = text_file
        self._text_processor = TextProcessor(text_file.text)

    def split_files_with_separators_starting_and_name(
        self, separators: List[SearchConfiguration]
    ) -> List[TextFile]:
        # TODO: Create naming strategies
        # TODO: Create split strategies (matching start, matching end)
        # TODO: Simplify by using List[Matching] as argument
        matchings = self.search_matchings_of_patterns(patterns=separators)
        matchings.sort(key=lambda matching: matching.start)

        split_positions = [matching.start for matching in matchings]

        splitted_texts = self._text_processor.split_at_positions(
            split_positions
        )

        # TODO: matchings and splitted texts can have different sizes
        return [
            TextFile(text=text, path=Path(matching.pattern_name))
            for matching, text in zip(matchings, splitted_texts)
        ]

    def get_matchings_by_patterns(
        self, patterns: List[SearchConfiguration]
    ) -> Dict[str, List[SimpleMatching]]:
        return {
            pattern.name: self.search_matchings_of_pattern(pattern)
            for pattern in patterns
        }

    def search_matchings_of_patterns(
        self,
        patterns: List[SearchConfiguration],
    ) -> List[SimpleMatching]:
        line_matchings: List[SimpleMatching] = []
        for pattern in patterns:
            line_matchings.extend(self.search_matchings_of_pattern(pattern))
        return line_matchings

    def search_matchings_of_pattern(
        self,
        pattern: SearchConfiguration,
    ) -> List[SimpleMatching]:
        return self._text_processor.find_matchings_of_pattern(pattern=pattern)
