from typing import List

from src.replace_configuration import ReplaceConfiguration
from src.search_configuration import SearchConfiguration
from src.text_file import TextFile
from src.text_processor import TextProcessor

REPLACEMENTS: List[ReplaceConfiguration] = [
    ReplaceConfiguration(
        search_configuration=SearchConfiguration(
            regex_pattern=r"![Normal parameter passing table]"
            r'(./param-passing-normal.png "Normal parameter passing")',
            name="image_1",
        ),
        replacement="![Normal parameter passing table]"
        '(../public/param-passing-normal.png "Normal parameter passing")',
    ),
    ReplaceConfiguration(
        search_configuration=SearchConfiguration(
            regex_pattern=r"![Advanced parameter passing table]"
            r'(./param-passing-advanced.png "Advanced parameter passing")',
            name="image_1",
        ),
        replacement="![Advanced parameter passing table]"
        '(../public/param-passing-advanced.png "Advanced parameter passing")',
    ),
]


def replace_multiple_patterns_of_file(file: TextFile) -> TextFile:
    text_processor = TextProcessor(file.text)

    for replacement_configuration in REPLACEMENTS:
        text_processor.substitute_pattern_with_replacement(
            pattern=replacement_configuration.search_configuration,
            replacement=replacement_configuration.replacement,
        )

    return TextFile(text=text_processor.get_text(), path=file.path)