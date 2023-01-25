#!/usr/bin/env python3
"""
LRUCache module
"""

from datetime import datetime
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Cache class
    """

    def __init__(self):
        super().__init__()
        self._keys = {}

    def put(self, key, item):
        """
        Cache an item
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self._keys[key] = {"val": 0, "time": datetime.now()}
                self.cache_data[key] = item
            else:
                for k, v in self._keys.items():
                    self._keys[k]["val"] += 1
                self._keys[key] = {"val": 0, "time": datetime.now()}
                self.cache_data[key] = item
            # print(self._keys)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = {k: v for k, v in self._keys.items()
                           if v["val"] == max(self._keys.values(),
                           key=lambda x: x['val'])["val"]}
                key = [k for k, v in lru_key.items()
                       if v["time"] == min(lru_key.values(),
                                           key=lambda x: x['time'])["time"]]
                self._keys.pop(key[0])
                self.cache_data.pop(key[0])
                print("DISCARD: {}".format(key[0]))

    def get(self, key):
        """
        Retrieve an item
        """
        if key in self._keys:
            self._keys[key] = {"val": 0, "time": datetime.now()}
            # print(self._keys)
        return self.cache_data.get(key, None)
