import re

from pydantic import BaseModel


class SearchConfiguration(BaseModel):
    name: str
    regex: re.Pattern

    def __init__(self, regex_pattern: str, name: str) -> None:
        super().__init__(regex=re.compile(regex_pattern), name=name)

    def get_regex(self):
        return self.regex

    def get_pattern(self):
        return self.regex.pattern

    # pylint: disable=too-few-public-methods
    class Config:
        arbitrary_types_allowed = True

    # pylint: enable=too-few-public-methods
