#!/usr/bin/python3
"""
this is a task on the
FIFO caching
"""


from base_caching import BaseCaching
from typing import OrderedDict


class LRUCache(BaseCaching):
    """
    this is a class that put and
    get items stored in a cache
    in a FIFO order
    """
    def __init__(self):
        """
        method overloading
        """
        super().__init__()
        self.caches_now = OrderedDict()

    def put(self, key, item):
        """
        this adds the key to the
        dictionary in from the
        parent class basing on
        BaseCaching.MAX_ITEMS
        """
        if key and item:
            self.caches_now[key] = item
            self.caches_now.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # get the first key in the array in their order
            item_removed = next(iter(self.caches_now))
            del self.cache_data[item_removed]
            print("DISCARD:", item_removed)

        if len(self.caches_now) > BaseCaching.MAX_ITEMS:
            self.caches_now.popitem(last=False)

    def get(self, key):
        """
        this returns the value
        related to the key
        """
        if key in self.cache_data:
            self.caches_now.move_to_end(key)
            return self.cache_data[key]
        return None
