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
class Delimiter:
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

class DelimitersRegistry:
    def __init__(self, delimiters: List[Delimiter]) -> None:
        self._delimiters: List[Delimiter] = delimiters

    def get_values(self) -> List[str]:
         return [delimiter.value for delimiter in self._delimiters]


file_starter_delimiters = DelimitersRegistry([
    Delimiter(name='main', value='name="main"'),
    Delimiter(name='abstract', value='name="S-abstract"'),
    Delimiter(name='introduction', value='name="S-introduction"')
])

lines_of_delimiters = find_lines_that_cointains_strings(lines, file_starter_delimiters.get_values())

print(lines_of_delimiters)