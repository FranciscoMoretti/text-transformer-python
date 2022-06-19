import re

from pydantic import BaseModel


# pylint: disable=too-few-public-methods
class Matching(BaseModel):
    pattern_name: str
    line_number: int
    match: re.Match

    class Config:
        arbitrary_types_allowed = True


# pylint: enable=too-few-public-methods
