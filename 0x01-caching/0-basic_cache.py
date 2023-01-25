#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache class
    """

    def put(self, key, item):
        """
        Cache an item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item
        """
        return self.cache_data.get(key, None)
