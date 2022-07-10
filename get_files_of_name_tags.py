import sys
from typing import List, Optional

from src.file_processor import FileProcessor
from src.matching import SimpleMatching
from src.search_configuration import SearchConfiguration
from src.text_file import TextFile


def get_filenames_of_name_tags(files: List[TextFile]):

    name_tag_pattern = SearchConfiguration(
        name="name_tag", regex_pattern=r'.*name="(?P<tag>[A-Za-z0-9-]*)".*'
    )

    tag_matchings_of_filenames = {
        file.path.stem: FileProcessor(file).search_matchings_of_pattern(
            name_tag_pattern
        )
        for file in files
    }

    def matching_list_to_value_of_match_group_list(
        matching_list: List[SimpleMatching], match_group_name: str
    ) -> List[Optional[str]]:
        return [
            matching_to_group_name_value(matching, match_group_name)
            for matching in matching_list
        ]

    def matching_to_group_name_value(
        matching: SimpleMatching, match_group_name: str
    ) -> Optional[str]:
        if match := name_tag_pattern.regex.match(matching.text):
            return match.groupdict().get(match_group_name)
        return None

    name_tags_of_filenames = {
        filename: matching_list_to_value_of_match_group_list(
            matching_list=matchings, match_group_name="tag"
        )
        for filename, matchings in tag_matchings_of_filenames.items()
    }

    name_tags_and_filenames = list(
        map(reversed, name_tags_of_filenames.items())
    )

    filenames_of_tag_names = {}
    tag_set = set()
    for (tag_names, filename) in name_tags_and_filenames:
        for tag_name in tag_names:
            filenames_of_tag_names[tag_name] = filename
            if tag_name not in tag_set:
                tag_set.add(tag_name)
            else:
                print("Should not have repeated tag names")
                sys.exit()
    return filenames_of_tag_names
