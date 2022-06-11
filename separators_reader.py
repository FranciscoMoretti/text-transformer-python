import json
from pathlib import Path
from typing import Dict, List

from separators import Separator, SeparatorList


class SeparatorsReader:
    @staticmethod
    def from_json_file(filepath: Path) -> SeparatorList:
        data = None
        with open(filepath, encoding="utf-8") as open_file:
            data = json.load(open_file)
        return SeparatorsReader.from_list_of_dictionaries(data)

    @staticmethod
    def from_list_of_dictionaries(list_of_dict: List[Dict[str, str]]):
        return SeparatorList([Separator(**dictionary) for dictionary in list_of_dict])
