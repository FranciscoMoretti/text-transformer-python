from collections import UserList
import inspect
import re
from typing import List

from pydantic import BaseModel, validator


class Pattern(BaseModel):
    name: str
    value: re.Pattern

    def __init__(self, value: str, name: str, **data) -> None:
        super().__init__(value=re.compile(value), name=name)

    def get_regex(self):
        return self.value

    def get_value(self):
        return self.value.pattern

    # pylint: disable=too-few-public-methods
    class Config:
        arbitrary_types_allowed = True

    # pylint: enable=too-few-public-methods


print(inspect.signature(Pattern))


class PatternList(UserList):
    def __init__(self, initlist=None) -> None:
        super().__init__(initlist)
        self.data: List[Pattern]

    def get_values(self) -> List[str]:
        return [pattern.get_value() for pattern in self.data]

    def get_regexps(self) -> List[re.Pattern]:
        return [pattern.get_regex() for pattern in self.data]
