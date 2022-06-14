from pathlib import Path
from typing import Dict, List

from separators_reader import SeparatorsReader
from text_line import TextLine
from virtual_file import VirtualFileIO
from virtual_file_processor import VirtualFileProcessor

INPUT_TEXT_FILE_PATH = Path(".sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path(".sandbox/separators.json")

input_file = VirtualFileIO.read_from_path(INPUT_TEXT_FILE_PATH)

file_processor = VirtualFileProcessor(input_file)


def find_lines_that_contains_strings(
    lines: List[str], match_patterns: List[str]
) -> Dict[str, List[TextLine]]:
    lines_by_match_pattern: Dict[str, List[TextLine]] = {
        match_pattern: [] for match_pattern in match_patterns
    }
    for line_number, line_text in enumerate(lines):
        for match_pattern in match_patterns:
            if match_pattern in line_text:
                lines_by_match_pattern[match_pattern].append(
                    TextLine(text=line_text, line_number=line_number)
                )
    return lines_by_match_pattern


file_starter_separators = SeparatorsReader.from_json_file(INPUT_SEPARATORS_FILE_PATH)

lines_of_separators = file_processor._find_lines_that_contains_pattern(
    file_starter_separators
)

print(lines_of_separators)
