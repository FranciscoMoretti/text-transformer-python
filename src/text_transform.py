from pathlib import Path

from src.pattern_registry import PatternRegistry
from src.patterns_reader import PatternsReader
from src.utils import all_items_have_one_item_in_them
from src.virtual_file import VirtualFileIO
from src.virtual_file_processor import VirtualFileProcessor

INPUT_TEXT_FILE_PATH = Path(".sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path(".sandbox/separators.json")
OUTPUT_DIRECTORY_PATH = Path(".sandbox/output")

file_starter_separators = PatternsReader.from_json_file(
    INPUT_SEPARATORS_FILE_PATH
)
separator_registry = PatternRegistry(patterns=file_starter_separators)

input_file = VirtualFileIO.read_from_path(INPUT_TEXT_FILE_PATH)
file_processor = VirtualFileProcessor(input_file)
lines_of_separators = file_processor.get_matched_lines_by_patterns(
    separator_registry
)

assert all_items_have_one_item_in_them(
    list_of_lists=list(lines_of_separators.values())
)

separated_files = file_processor.split_files_with_separators(
    separators=separator_registry
)

for file in separated_files:
    file.path = Path.joinpath(OUTPUT_DIRECTORY_PATH, file.path).with_suffix(
        ".md"
    )

for file in separated_files:
    VirtualFileIO.save_to_real_file(virtual_file=file)
