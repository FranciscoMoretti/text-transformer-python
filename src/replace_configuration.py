from pydantic import BaseModel

from src.search_configuration import SearchConfiguration


class ReplaceConfiguration(BaseModel):
    search_configuration: SearchConfiguration
    replacement: str
