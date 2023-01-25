#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Cache class
    """

    def put(self, key, item):
        """
        Cache an item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-2]
                last = self.cache_data.pop(last_key)
                print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        Retrieve an item
        """
        return self.cache_data.get(key, None)
