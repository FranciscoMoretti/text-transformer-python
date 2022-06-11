# Python program to
# demonstrate with
# statement

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from separators_reader import SeparatorsReader
from virtual_file import VirtualFileIO

INPUT_TEXT_FILE_PATH = Path("./.sandbox/CppCoreGuidelines.md")
INPUT_SEPARATORS_FILE_PATH = Path("./.sandbox/separators.json")

input_file = VirtualFileIO.read_from_path(INPUT_TEXT_FILE_PATH)


@dataclass
class TextLine:
    text: str
    line_number: int


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

lines_of_separators = find_lines_that_contains_strings(
    input_file.lines, file_starter_separators.get_values()
)

print(lines_of_separators)
