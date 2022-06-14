from pathlib import Path

from separators_reader import SeparatorsReader
from utils import all_items_have_one_item_in_them
from virtual_file import VirtualFileIO
from virtual_file_processor import VirtualFileProcessor

INPUT_TEXT_FILE_PATH = Path(".sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path(".sandbox/separators.json")


file_starter_separators = SeparatorsReader.from_json_file(INPUT_SEPARATORS_FILE_PATH)

input_file = VirtualFileIO.read_from_path(INPUT_TEXT_FILE_PATH)
file_processor = VirtualFileProcessor(input_file)
lines_of_separators = file_processor.get_text_lines_that_match_separators(
    file_starter_separators
)

assert all_items_have_one_item_in_them(list_of_lists=list(lines_of_separators.values()))


print(lines_of_separators)
