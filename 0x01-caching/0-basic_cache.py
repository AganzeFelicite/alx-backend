#!/usr/bin/python3
"""
this is a module
that get and put into a cache some
values
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    this is class that inherites
    from the baseCaching
    """
    def __init__(self):
        """
        init method
        """
        super().__init__()

    def put(self, key, item):
        """
        this method that puts
        values in the cache data
        dictionary from the parent
        class
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        this returns the value in the
        self.cache_data related
        to the key in the dic
        """
        if key is not None:
            if key in self.cache_data.keys():
                return self.cache_data[key]
        return None
