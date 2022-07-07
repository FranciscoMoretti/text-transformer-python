import json
from pathlib import Path
from typing import Dict, List

from src.search_configuration import SearchConfiguration


class PatternsReader:
    @staticmethod
    def from_json_file(filepath: Path) -> List[SearchConfiguration]:
        data = None
        with open(filepath, encoding="utf-8") as open_file:
            data = json.load(open_file)
        return PatternsReader.from_list_of_dictionaries(data)

    @staticmethod
    def from_list_of_dictionaries(list_of_dict: List[Dict[str, str]]):
        return [
            SearchConfiguration(**dictionary) for dictionary in list_of_dict
        ]
