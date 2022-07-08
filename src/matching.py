from pydantic import BaseModel


class SimpleMatching(BaseModel):
    pattern_name: str
    text: str
    start: int
    end: int
