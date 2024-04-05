#!/usr/bin/env python3
"""Simple helper function arguments page and page_size"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """"
    returns a tuple with the idnex of the parameters given
    """
    if page == 1:
        start_index = 0
        return tuple((start_index, page_size))
    else:
        start_index = (page * page_size) - page_size
        end_index = page * page_size
        return tuple((start_index, end_index))
