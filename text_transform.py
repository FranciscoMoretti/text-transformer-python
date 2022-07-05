import re
import sys
from pathlib import Path
from typing import List, Optional

from src.matching import Matching
from src.named_patterns import SearchConfiguration
from src.pattern_registry import PatternRegistry
from src.patterns_reader import PatternsReader
from src.text_processor import TextProcessor
from src.virtual_file import VirtualFileIO
from src.virtual_file_processor import VirtualFileProcessor


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


INPUT_TEXT_FILE_PATH = Path(".sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path(".sandbox/separators.json")
OUTPUT_DIRECTORY_PATH = Path(".sandbox/output")

file_starter_separators = PatternsReader.from_json_file(
    INPUT_SEPARATORS_FILE_PATH
)
separator_registry = PatternRegistry(patterns=file_starter_separators)

input_file = VirtualFileIO.read_from_path(INPUT_TEXT_FILE_PATH)
file_processor = VirtualFileProcessor(input_file)

separated_files = file_processor.split_files_with_separators(
    separators=separator_registry
)

# Experiment of testing the new api and draft for FileProcessor
text_processor = TextProcessor(text="".join(input_file.lines))
separators_matchings_lists = [
    text_processor.find_matchings_of_pattern(separator)
    for separator in file_starter_separators
]
separators_matchings = flatten(separators_matchings_lists)
separators_matchings.sort(key=lambda x: x.start)
separated_texts = text_processor.split_at_positions(
    [matching.start for matching in separators_matchings]
)

filenames = [file.path.stem for file in separated_files]

files_of_filenames = {file.path.name: file for file in separated_files}

name_tag_pattern = SearchConfiguration(
    name="name_tag", regex_pattern=r'.*name="(?P<tag>[A-Za-z0-9-]*)".*'
)

matchings_of_filenames = {
    file.path.stem: VirtualFileProcessor(file).search_matchings_of_pattern(
        name_tag_pattern
    )
    for file in separated_files
}


def matching_list_to_value_of_match_group_list(
    matching_list: List[Matching], match_group_name: str
) -> List[Optional[str]]:
    return [
        matching_to_group_name_value(matching, match_group_name)
        for matching in matching_list
    ]


def matching_to_group_name_value(
    matching: Matching, match_group_name: str
) -> Optional[str]:
    return matching.match.groupdict().get(match_group_name)


name_tags_of_filenames = {
    filename: matching_list_to_value_of_match_group_list(
        matching_list=matchings, match_group_name="tag"
    )
    for filename, matchings in matchings_of_filenames.items()
}

tag_names_and_filenames = list(map(reversed, name_tags_of_filenames.items()))

filenames_of_tags = {}
tag_set = set()
for (tag_names, filename) in tag_names_and_filenames:
    for tag_name in tag_names:
        filenames_of_tags[tag_name] = filename
        if tag_name not in tag_set:
            tag_set.add(tag_name)
        else:
            print("Should not have repeated tag names")
            sys.exit()


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


for relative_tag, absolute_tag in absolute_tag_of_relative_tag.items():
    pattern = SearchConfiguration(
        name="name_tag",
        regex_pattern=rf".*\[.*\]\((?P<relative>#{relative_tag})\).*",
    )
    file_processor.substitute_pattern_with_replacement(
        pattern=pattern,
        replacement=replace_relative_tag_by_absolute_tag_in_match,
    )

separated_files_with_absolute_references = (
    file_processor.split_files_with_separators(separators=separator_registry)
)

for file in separated_files_with_absolute_references:
    file.path = Path.joinpath(OUTPUT_DIRECTORY_PATH, file.path).with_suffix(
        ".mdx"
    )
for file in separated_files_with_absolute_references:
    VirtualFileIO.save_to_real_file(virtual_file=file)
