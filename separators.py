from dataclasses import dataclass
from typing import List

@dataclass
class Separator:
    name: str
    value: str

class SeparatorsRegistry:
    def __init__(self, delimiters: List[Separator]) -> None:
        self._separators: List[Separator] = delimiters

    def get_values(self) -> List[str]:
         return [separator.value for separator in self._separators]

