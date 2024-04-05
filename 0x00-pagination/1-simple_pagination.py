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
        index_tuple = Server.index_range(page, page_size)
        start, end = index_tuple[0], index_tuple[1]
        return Server.dataset(self)[start: end]

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
