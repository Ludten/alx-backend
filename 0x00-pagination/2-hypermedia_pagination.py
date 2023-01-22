#!/usr/bin/env python3
"""
Helper module
"""

import csv
import math
from typing import List, Mapping, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    take two integer and return a tuple with a floor or
    round of the first and the second

    Args:
        page (int)
        page_size (int)

    Return:
        Tuple
    """
    nextpage: int = page * page_size
    return (nextpage - page_size, nextpage)


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
        Return paginated list
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        pagie = index_range(page, page_size)
        if pagie[0] > len(self.dataset()) - 1:
            return []
        return self.dataset()[pagie[0]:pagie[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Mapping:
        """
        Return paginated dictionary
        """
        pagie = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(pagie),
            "page": page,
            "data": pagie,
            "next_page": None if page >= total_pages else page + 1,
            "prev_page": None if page - 1 <= 0 else page - 1,
            "total_pages": total_pages
        }
