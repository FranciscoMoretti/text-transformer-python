from src.search_configuration import SearchConfiguration
from src.text_file import TextFile
from src.text_processor import TextProcessor


def replace_multiple_patterns_of_file(file: TextFile) -> TextFile:
    text_processor = TextProcessor(file.text)

    text_processor.substitute_pattern_with_replacement(
        pattern=SearchConfiguration(
            regex_pattern=r"![Normal parameter passing table]"
            r'(./param-passing-normal.png "Normal parameter passing")',
            name="image_1",
        ),
        replacement="![Normal parameter passing table]"
        '(../public/param-passing-normal.png "Normal parameter passing")',
    )

    return TextFile(text=text_processor.get_text(), path=file.path)
