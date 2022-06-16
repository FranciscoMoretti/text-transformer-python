from pydantic import BaseModel


class TextLine(BaseModel):
    text: str
    line_number: int
