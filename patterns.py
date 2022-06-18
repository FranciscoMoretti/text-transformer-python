from collections import UserList
import re
from typing import List

from pydantic import BaseModel


class Pattern(BaseModel):
    name: str
    value: str

    def get_regex(self):
        return re.compile(self.value)

    def get_value(self):
        return self.value


class PatternList(UserList):
    def __init__(self, initlist=None) -> None:
        super().__init__(initlist)
        self.data: List[Pattern]

    def get_values(self) -> List[str]:
        return [pattern.get_value() for pattern in self.data]

    def get_regexps(self) -> List[re.Pattern]:
        return [pattern.get_regex() for pattern in self.data]
