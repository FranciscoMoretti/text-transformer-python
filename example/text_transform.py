from pathlib import Path
from typing import List

from example.configure_output_file_paths import configure_output_file_paths
from example.get_files_of_name_tags import get_filenames_of_name_tags
from example.replace_relative_tags_with_absolute_tags_in_file import (
    replace_relative_tags_with_absolute_tags_in_file,
)

from src.recipes import split_file_with_separators
from src.search_configuration import SearchConfiguration
from src.search_configurations_reader import SearchConfigurationsReader
from src.text_file_io import TextFileIO

INPUT_TEXT_FILE_PATH = Path(".sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path(".sandbox/separators.json")
OUTPUT_DIRECTORY_PATH = Path(".sandbox/output")
OUTPUT_FILE_EXTENSION = ".mdx"

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


edited_file = replace_relative_tags_with_absolute_tags_in_file(
    input_file, absolute_tag_of_relative_tag
)

separated_files_with_absolute_references = split_file_with_separators(
    edited_file, file_separators
)

files = configure_output_file_paths(
    files=separated_files_with_absolute_references,
    prefix_path=OUTPUT_DIRECTORY_PATH,
    file_suffix=OUTPUT_FILE_EXTENSION,
)

for file in files:
    TextFileIO.save_to_real_file(file)
