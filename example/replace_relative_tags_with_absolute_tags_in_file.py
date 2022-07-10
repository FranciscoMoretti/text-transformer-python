import re

from src.search_configuration import SearchConfiguration
from src.text_file import TextFile
from src.text_processor import TextProcessor


def replace_relative_tags_with_absolute_tags_in_file(
    input_file, absolute_tag_of_relative_tag
):
    def replace_relative_tag_by_absolute_tag_in_match(
        match_object: re.Match,
    ) -> str:
        relative_name = match_object.groupdict()["relative"]
        absolute_name = absolute_tag_of_relative_tag[relative_name.lstrip("#")]
        return match_object.string.replace(relative_name, absolute_name)

    input_file_text_processor = TextProcessor(input_file.text)

    for relative_tag in absolute_tag_of_relative_tag.keys():
        pattern = SearchConfiguration(
            name="name_tag",
            regex_pattern=rf".*\[.*\]\((?P<relative>#{relative_tag})\).*",
        )
        input_file_text_processor = TextProcessor(
            input_file_text_processor.substitute_pattern_with_replacement(
                pattern=pattern,
                replacement=replace_relative_tag_by_absolute_tag_in_match,
            )
        )

    return TextFile(
        text=input_file_text_processor.get_text(), path=input_file.path
    )
