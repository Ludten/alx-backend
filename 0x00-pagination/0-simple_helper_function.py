#!/usr/bin/env python3
"""
Helper module
"""

from typing import Tuple


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
    j: int = 0
    if page > 1:
        for i in range(0, page):
            j = j + 10
    return (j, page_size + j)
