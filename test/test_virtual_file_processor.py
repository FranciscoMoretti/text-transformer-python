from copy import deepcopy
from pathlib import Path

from src.named_patterns import NamedPattern, NamedPatternList
from src.pattern_registry import PatternRegistry
from src.text_line import TextLine
from src.utils import all_items_have_one_item_in_them
from src.virtual_file import VirtualFile
from src.virtual_file_processor import VirtualFileProcessor

MULTILINE_CONTENT = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n",
    "Line 4\n",
    "Line 5\n",
    "Line 6\n",
    "Line 7\n",
]
VIRTUAL_FILE = VirtualFile(lines=MULTILINE_CONTENT, path=Path())


def test_get_raw_lines_in_range():
    file_processor = VirtualFileProcessor(VIRTUAL_FILE)
    assert (
        file_processor.get_raw_lines_in_range(end_line=2)
        == MULTILINE_CONTENT[:2]
    )
    assert (
        file_processor.get_raw_lines_in_range(start_line=2)
        == MULTILINE_CONTENT[2:]
    )
    assert (
        file_processor.get_raw_lines_in_range(start_line=1, end_line=2)
        == MULTILINE_CONTENT[1:2]
    )


def test_get_matchings_of_patterns():
    file_processor = VirtualFileProcessor(VIRTUAL_FILE)
    patterns = NamedPatternList(
        [
            NamedPattern(name="foo", value="Line 1"),
            NamedPattern(name="bar", value="Line 3"),
        ]
    )
    pattern_registry = PatternRegistry(patterns)
    matched_lines = file_processor.get_matched_lines_by_patterns(
        patterns=pattern_registry
    )
    assert all_items_have_one_item_in_them(list(matched_lines.values()))
    assert matched_lines["foo"][0] == TextLine(
        text=MULTILINE_CONTENT[0], line_number=0
    )
    assert matched_lines["bar"][0] == TextLine(
        text=MULTILINE_CONTENT[2], line_number=2
    )


def test_split_files_by_separators():
    file_processor = VirtualFileProcessor(VIRTUAL_FILE)
    separators = NamedPatternList(
        [
            NamedPattern(name="foo", value="Line 1"),
            NamedPattern(name="bar", value="Line 3"),
            NamedPattern(name="baz", value="Line 6"),
        ]
    )
    pattern_registry = PatternRegistry(separators)
    output_files = file_processor.split_files_with_separators(
        separators=pattern_registry
    )
    assert len(output_files) == 3
    assert all(isinstance(file, VirtualFile) for file in output_files)
    assert output_files[1].path == Path("bar")
    assert output_files[1].lines == MULTILINE_CONTENT[2:5]


def test_search_matchings_of_pattern():
    file_processor = VirtualFileProcessor(VIRTUAL_FILE)
    pattern = NamedPattern(name="bar", value="Line 3")

    matchings = file_processor.search_matchings_of_pattern(pattern=pattern)
    assert len(matchings) == 1
    assert matchings[0].pattern_name == "bar"


def test_search_matchings_of_regex_pattern():
    file_with_regex = deepcopy(VIRTUAL_FILE)
    file_with_regex.lines.insert(3, '## <a name="SS-aims"></a>In.aims: Aims')
    file_processor = VirtualFileProcessor(file_with_regex)
    pattern = NamedPattern(
        name="foo", value=r'.*name="(?P<bar>[A-Za-z0-9-]*)".*'
    )

    matchings = file_processor.search_matchings_of_pattern(pattern=pattern)
    assert len(matchings) == 1
    assert matchings[0].pattern_name == "foo"
    assert matchings[0].match.groupdict()["bar"] == "SS-aims"


def test_substitute_pattern_with_replacement():
    file_processor = VirtualFileProcessor(VIRTUAL_FILE)
    pattern = NamedPattern(name="bar", value="Line 3")

    file_processor.substitute_pattern_with_replacement(
        pattern=pattern, replacement="Line new"
    )
    assert file_processor.virtual_file.lines[2] == "Line new\n"
