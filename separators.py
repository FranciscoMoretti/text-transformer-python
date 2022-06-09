from collections import UserList
from dataclasses import dataclass
from typing import List


@dataclass
class Separator:
    name: str
    value: str


class SeparatorList(UserList):
    def get_values(self) -> List[str]:
        return [separator.value for separator in self.data]
