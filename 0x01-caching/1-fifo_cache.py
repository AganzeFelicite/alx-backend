#!/usr/bin/python3
"""
this is a task on the
FIFO caching
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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
            self.cache_data[key] = item
            if key not in self.caches_now:
                self.caches_now.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                Key = self.caches_now.pop(0)
                del self.cache_data[Key]
                print(f"DISCARD:{Key}")

    def get(self, key):
        """
        this returns the value
        related to the key
        """
        return self.cache_data.get(key) or None
