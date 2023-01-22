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
    nextpage: int = page * page_size
    return (nextpage - page_size, nextpage)
