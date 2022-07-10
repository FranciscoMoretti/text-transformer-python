from typing import List

from src.file_processor import FileProcessor
from src.search_configuration import SearchConfiguration
from src.text_file import TextFile


def split_file_with_separators(
    file: TextFile, separators: List[SearchConfiguration]
) -> List[TextFile]:
    input_file_processor = FileProcessor(file)
    return input_file_processor.split_files_with_separators_starting_and_name(
        separators=separators
    )
