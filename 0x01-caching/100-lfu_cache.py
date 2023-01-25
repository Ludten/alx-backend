#!/usr/bin/env python3
"""
LFUCache module
"""

from datetime import datetime
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Cache class
    """

    def __init__(self):
        super().__init__()
        self._keys = {}

    def put(self, key, item):
        """
        Cache an item
        """
        if key is not None and item is not None:
            if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
                if key not in self.cache_data:
                    LFU_key = {k: v
                               for k, v in self._keys.items()
                               if v["val"] == min(self._keys.values(),
                                                  key=lambda x: x[
                                   'val'])["val"]}
                    keyd = [k for k, v in LFU_key.items()
                            if v["time"] == min(LFU_key.values(),
                                                key=lambda x: x[
                                                    'time'])["time"]]
                    self._keys.pop(keyd[0])
                    self.cache_data.pop(keyd[0])
                    print("DISCARD: {}".format(keyd[0]))
            if key in self.cache_data:
                self._keys[key]["val"] += 1
                self.cache_data[key] = item
            else:
                self._keys[key] = {"val": 0, "time": datetime.now()}
                self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item
        """
        if key in self._keys:
            self._keys[key]["val"] += 1
        return self.cache_data.get(key, None)
