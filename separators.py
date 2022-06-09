from collections import UserList
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Separator:
    name: str
    value: str


class SeparatorList(UserList):
    def get_values(self) -> List[str]:
        return [separator.value for separator in self.data]

    @staticmethod
    def from_list_of_dictionaries(list_of_dict: List[Dict[str, str]]):
        return SeparatorList(
            [
                Separator(name=dictionary["name"], value=dictionary["value"])
                for dictionary in list_of_dict
            ]
        )
