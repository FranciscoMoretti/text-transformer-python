from itertools import tee
from typing import Any, List


def all_items_have_one_item_in_them(list_of_lists: List[List[Any]]) -> bool:
    return all(len(internal_list) == 1 for internal_list in list_of_lists)


# From https://docs.python.org/3/library/itertools.html#itertools.pairwise
def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
