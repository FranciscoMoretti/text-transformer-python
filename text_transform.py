# Python program to
# demonstrate with
# statement
  
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from separators import Separator, SeparatorsRegistry


L = ["Geeks\n", "for\n", "Geeks\n"]
  
  
# Writing to file
with open("myfile.txt", "w") as fp:
    fp.writelines(L)
  
  
# using readlines()
count = 0
print("Using readlines()")

lines: List[str] = []

@dataclass
class VirtualFile:
    lines: str
    path: Optional[Path] = None

class FileReader:
    @staticmethod
    def read_from_path(filepath: Path) -> VirtualFile:
        with open(filepath) as open_file:
            return VirtualFile(
                lines=open_file.readlines(),
                path=filepath
            )
        

input_file = FileReader.read_from_path("CppCoreGuidelines.md")

@dataclass
class Line:
    text: str
    number: int

def find_lines_that_cointains_strings(lines: List[str], match_patterns: List[str]) -> List[Line]:
    lines_by_match_pattern: Dict[str, List[str]] = {match_pattern: [] for match_pattern in match_patterns}
    for line_number, line_text  in enumerate(lines):
        for match_pattern in match_patterns:
            if match_pattern in line_text:
                lines_by_match_pattern[match_pattern].append(Line(text=line_text, number=line_number))
    return lines_by_match_pattern


file_starter_separators = SeparatorsRegistry([
    Separator(name='main', value='name="main"'),
    Separator(name='abstract', value='name="S-abstract"'),
    Separator(name='introduction', value='name="S-introduction"')
])

lines_of_separators = find_lines_that_cointains_strings(input_file.lines, file_starter_separators.get_values())

print(lines_of_separators)