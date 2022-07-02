from typing import List

from src.named_patterns import SearchConfigurationList


class PatternRegistry:
    def __init__(self, patterns: SearchConfigurationList) -> None:
        self.patterns = patterns

    def get_pattern_names(self) -> List[str]:
        return [pattern.name for pattern in self.patterns]
