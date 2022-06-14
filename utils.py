from typing import Any, List


def all_items_have_one_item_in_them(list_of_lists: List[List[Any]]) -> bool:
    return all(len(internal_list) == 1 for internal_list in list_of_lists)
