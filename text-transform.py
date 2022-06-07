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


file_starter_delimiters: List[Delimiter] = [
    Delimiter(name='main', value='name="main"'),
    Delimiter(name='abstract', value='name="S-abstract"'),
    Delimiter(name='introduction', value='name="S-introduction"')
]

lines_of_delimiters = find_lines_that_cointains_strings(lines, file_starter_delimiters) 



find_lines_that_cointains_string(lines, file_starter_delimiters, lines_by_delimiters)


print(lines_by_delimiters)