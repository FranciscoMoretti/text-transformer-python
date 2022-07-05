from io import StringIO


def line_iterator(raw_string: str):
    string = StringIO(raw_string)
    while True:
        new_line = string.readline()
        if new_line == "":
            break
        yield new_line.strip("\n")
