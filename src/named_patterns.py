import re
from collections import UserList
from typing import List

from pydantic import BaseModel


class NamedPattern(BaseModel):
    name: str
    regex: re.Pattern

    def __init__(self, value: str, name: str) -> None:
        super().__init__(regex=re.compile(value), name=name)

    def get_regex(self):
        return self.regex

    def get_pattern(self):
        return self.regex.pattern

    # pylint: disable=too-few-public-methods
    class Config:
        arbitrary_types_allowed = True

    # pylint: enable=too-few-public-methods


class NamedPatternList(UserList):
    def __init__(self, initlist=None) -> None:
        super().__init__(initlist)
        self.data: List[NamedPattern]

    def get_patterns(self) -> List[str]:
        return [pattern.get_pattern() for pattern in self.data]

    def get_regexps(self) -> List[re.Pattern]:
        return [pattern.get_regex() for pattern in self.data]
