import re
import sys
from pathlib import Path
from typing import List, Optional

from src.file_processor import FileProcessor
from src.matching import SimpleMatching
from src.recipes import split_file_with_separators
from src.search_configuration import SearchConfiguration
from src.search_configurations_reader import SearchConfigurationsReader
from src.text_file import TextFile
from src.text_file_io import TextFileIO
from src.text_processor import TextProcessor


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


INPUT_TEXT_FILE_PATH = Path(".sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path(".sandbox/separators.json")
OUTPUT_DIRECTORY_PATH = Path(".sandbox/output")

file_separators: List[
    SearchConfiguration
] = SearchConfigurationsReader.from_json_file(INPUT_SEPARATORS_FILE_PATH)

input_file = TextFileIO.read_from_path(INPUT_TEXT_FILE_PATH)

separated_files = split_file_with_separators(input_file, file_separators)

filenames_of_tags = get_filenames_of_name_tags(separated_files)


def relative_tag_to_absolute_tag(tag: str, path: str) -> str:
    return f"/{path}#{tag}"


absolute_tag_of_relative_tag = {
    tag: relative_tag_to_absolute_tag(tag, filename)
    for tag, filename in filenames_of_tags.items()
}


def replace_relative_tag_by_absolute_tag_in_match(
    match_object: re.Match,
) -> str:
    relative_name = match_object.groupdict()["relative"]
    absolute_name = absolute_tag_of_relative_tag[relative_name.lstrip("#")]
    return match_object.string.replace(relative_name, absolute_name)


input_file_text_processor = TextProcessor(input_file.text)

for relative_tag, absolute_tag in absolute_tag_of_relative_tag.items():
    pattern = SearchConfiguration(
        name="name_tag",
        regex_pattern=rf".*\[.*\]\((?P<relative>#{relative_tag})\).*",
    )
    input_file_text_processor = TextProcessor(
        input_file_text_processor.substitute_pattern_with_replacement(
            pattern=pattern,
            replacement=replace_relative_tag_by_absolute_tag_in_match,
        )
    )

separated_files_with_absolute_references = split_file_with_separators(
    TextFile(text=input_file_text_processor.get_text(), path=Path("")),
    file_separators,
)

for file_a in separated_files_with_absolute_references:
    file_a.path = Path.joinpath(
        OUTPUT_DIRECTORY_PATH, file_a.path
    ).with_suffix(".mdx")
for file_b in separated_files_with_absolute_references:
    TextFileIO.save_to_real_file(file_b)
