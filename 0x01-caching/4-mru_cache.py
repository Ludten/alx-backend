#!/usr/bin/env python3
"""
MRUCache module
"""

from datetime import datetime
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Cache class
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
                    MRU_key = {k: v
                               for k, v in self._keys.items()
                               if v["val"] == min(self._keys.values(),
                                                  key=lambda x: x[
                                   'val'])["val"]}
                    keyd = [k for k, v in MRU_key.items()
                            if v["time"] == max(MRU_key.values(),
                                                key=lambda x: x[
                                                    'time'])["time"]]
                    self._keys.pop(keyd[0])
                    self.cache_data.pop(keyd[0])
                    print("DISCARD: {}".format(keyd[0]))

            if key in self.cache_data:
                self._keys[key] = {"val": 0, "time": datetime.now()}
                self.cache_data[key] = item
            else:
                for k, v in self._keys.items():
                    self._keys[k]["val"] += 1
                self._keys[key] = {"val": 0, "time": datetime.now()}
                self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item
        """
        if key in self._keys:
            self._keys[key] = {"val": 0, "time": datetime.now()}
            # print(self._keys)
        return self.cache_data.get(key, None)
