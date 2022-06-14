from pathlib import Path

from separators_reader import SeparatorsReader
from utils import all_items_have_one_item_in_them, pairwise
from virtual_file import VirtualFile, VirtualFileIO
from virtual_file_processor import VirtualFileProcessor

INPUT_TEXT_FILE_PATH = Path(".sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path(".sandbox/separators.json")
OUTPUT_DIRECTORY_PATH = Path(".sandbox/output")

file_starter_separators = SeparatorsReader.from_json_file(INPUT_SEPARATORS_FILE_PATH)

input_file = VirtualFileIO.read_from_path(INPUT_TEXT_FILE_PATH)
file_processor = VirtualFileProcessor(input_file)
lines_of_separators = file_processor.get_text_lines_that_match_separators(
    file_starter_separators
)

assert all_items_have_one_item_in_them(list_of_lists=list(lines_of_separators.values()))

separated_files = []
for (current_key, current_lines), (_, next_lines) in pairwise(
    lines_of_separators.items()
):
    current_separator_name = current_key
    start_line_number = next(iter(current_lines)).line_number
    end_line_number = next(iter(next_lines)).line_number
    virtual_file = VirtualFile(
        path=Path.joinpath(OUTPUT_DIRECTORY_PATH, current_separator_name).with_suffix(
            ".md"
        ),
        lines=file_processor.get_raw_lines_in_range(start_line_number, end_line_number),
    )
    separated_files.append(virtual_file)

for file in separated_files:
    VirtualFileIO.save_to_real_file(virtual_file=file)
