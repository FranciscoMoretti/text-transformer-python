import re
from typing import Callable, Union

RegexReplacement = Union[str, Callable[[re.Match], str]]
