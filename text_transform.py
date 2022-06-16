from pathlib import Path

from patterns_reader import PatternsReader
from utils import all_items_have_one_item_in_them, pairwise
from virtual_file import VirtualFile, VirtualFileIO
from virtual_file_processor import VirtualFileProcessor

INPUT_TEXT_FILE_PATH = Path(".sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path(".sandbox/separators.json")
OUTPUT_DIRECTORY_PATH = Path(".sandbox/output")

file_starter_separators = PatternsReader.from_json_file(INPUT_SEPARATORS_FILE_PATH)

input_file = VirtualFileIO.read_from_path(INPUT_TEXT_FILE_PATH)
file_processor = VirtualFileProcessor(input_file)
lines_of_separators = file_processor.get_matched_lines_by_patterns(
    file_starter_separators
)

assert all_items_have_one_item_in_them(list_of_lists=list(lines_of_separators.values()))

separated_files = file_processor.split_files_with_separators(
    separators=file_starter_separators
)

for file in separated_files:
    file.path = Path.joinpath(OUTPUT_DIRECTORY_PATH, file.path).with_suffix(".md")

for file in separated_files:
    VirtualFileIO.save_to_real_file(virtual_file=file)
