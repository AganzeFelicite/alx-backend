#!/usr/bin/env python3

"""
Contains a MRUCaching class
"""

from base_caching import BaseCaching
from collections import deque, OrderedDict


class MRUCache(BaseCaching):
    """
    LRUcache class that uses the LRU algorithm and inherits from
        Basecaching
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds a new key-value pair to the cache
        Args:
            Key: Key to be added
            item: Value of the added key
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                k, v = self.cache_data.popitem()
                print(f"DISCARD: {k}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Retrieves the value of the key provided from the dict
        Returns none if the key is empty or is not valid key in the dict
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
            return self.cache_data[key]
        elif not key or key not in self.cache_data:
            return None
