from src.search_configuration import SearchConfiguration
from src.text_file import TextFile
from src.text_processor import TextProcessor


def replace_relative_tags_with_absolute_tags_in_file(
    input_file, absolute_tag_of_relative_tag
):

    input_file_text_processor = TextProcessor(input_file.text)

    for relative_tag, absolute_tag in absolute_tag_of_relative_tag.items():
        print(f"running for tag: {relative_tag} ")
        regex_pattern = rf"\[(?P<link>.*)\]\((?P<relative>#{relative_tag})\)"
        pattern = SearchConfiguration(
            name="name_tag",
            regex_pattern=regex_pattern,
        )
        input_file_text_processor.substitute_pattern_with_replacement(
            pattern=pattern, replacement=rf"[(\g<link>)]({absolute_tag})"
        )

    return TextFile(
        text=input_file_text_processor.get_text(), path=input_file.path
    )
