# Python program to
# demonstrate with
# statement
  
from typing import List


L = ["Geeks\n", "for\n", "Geeks\n"]
  
  
# Writing to file
with open("myfile.txt", "w") as fp:
    fp.writelines(L)
  
  
# using readlines()
count = 0
print("Using readlines()")

lines: List[str] = []

with open("myfile.txt") as fp:
    lines = fp.readlines()

lines_by_section = lines