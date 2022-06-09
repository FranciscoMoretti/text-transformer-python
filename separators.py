from collections import UserList
from typing import Dict, List

from pydantic import BaseModel


class Separator(BaseModel):
    name: str
    value: str


class SeparatorList(UserList):
    def __init__(self, initlist=None) -> None:
        super().__init__(initlist)
        self.data: List[Separator]

    def get_values(self) -> List[str]:
        return [separator.value for separator in self.data]

    @staticmethod
    def from_list_of_dictionaries(list_of_dict: List[Dict[str, str]]):
        return SeparatorList([Separator(**dictionary) for dictionary in list_of_dict])
