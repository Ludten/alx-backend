#!/usr/bin/env python3
"""
BasicCache module
"""

from typing import Any, Union
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache class
    """

    def put(self, key: Any, item: Any) -> None:
        """
        Cache an item
        """
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key: Any) -> Union[Any, None]:
        """
        Retrieve an item
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
