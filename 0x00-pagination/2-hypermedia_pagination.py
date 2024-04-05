#!/usr/bin/env python3
"""Implement pagination on a csv file"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        implement pagination
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index_tuple = index_range(page, page_size)
        start, end = index_tuple[0], index_tuple[1]
        return Server.dataset(self)[start: end]

    def get_hyper(self, page: int, page_size: int) -> dict:
        """
        returns a dictionary
        """
        data = Server.get_page(page, page_size)
        dataset = Server.dataset(self)
        pages = math.ceil(len(dataset) / page_size)
        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1 if page < pages else None,
                "prev_page": page - 1 if pages >= 1 else None,
                "total_pages": pages
                }


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
