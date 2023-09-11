#!/usr/bin/python3
"""
this is a task on the
FIFO caching
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
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
        self.caches_now = []

    def put(self, key, item):
        """
        this adds the key to the
        dictionary in from the
        parent class basing on
        BaseCaching.MAX_ITEMS
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.caches_now.remove(key)
                else:
                    del self.cache_data[self.caches_now[self.MAX_ITEMS - 1]]
                    item_discarded = self.caches_now.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.caches_now.append(key)

    def get(self, key):
        """
        this returns the value
        related to the key
        """
        return self.cache_data.get(key) or None
