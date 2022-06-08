# Python program to
# demonstrate with
# statement
  
from ast import Del
from dataclasses import dataclass
from typing import Dict, List


L = ["Geeks\n", "for\n", "Geeks\n"]
  
  
# Writing to file
with open("myfile.txt", "w") as fp:
    fp.writelines(L)
  
  
# using readlines()
count = 0
print("Using readlines()")

lines: List[str] = []

with open("CppCoreGuidelines.md") as fp:
    lines = fp.readlines()

@dataclass
class Separator:
    name: str
    value: str

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

class SeparatorsRegistry:
    def __init__(self, delimiters: List[Separator]) -> None:
        self._separators: List[Separator] = delimiters

    def get_values(self) -> List[str]:
         return [separator.value for separator in self._separators]


file_starter_separators = SeparatorsRegistry([
    Separator(name='main', value='name="main"'),
    Separator(name='abstract', value='name="S-abstract"'),
    Separator(name='introduction', value='name="S-introduction"')
])

lines_of_separators = find_lines_that_cointains_strings(lines, file_starter_separators.get_values())

print(lines_of_separators)