from collections import UserList
from typing import List

from pydantic import BaseModel


class Pattern(BaseModel):
    name: str
    value: str


class PatternList(UserList):
    def __init__(self, initlist=None) -> None:
        super().__init__(initlist)
        self.data: List[Pattern]

    def get_values(self) -> List[str]:
        return [pattern.value for pattern in self.data]
