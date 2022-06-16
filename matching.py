from pydantic import BaseModel

from text_line import TextLine


class Matching(BaseModel):
    pattern_name: str
    text_line: TextLine
