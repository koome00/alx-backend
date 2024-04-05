#!/usr/bin/python3
""" caching implementation"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """
    def __init__(self):
        """initialize class"""
        super().__init__()

    def put(self, key, item):
        """add an item to cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = sorted(self.cache_data)[0]
            self.cache_data.pop(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ Get an item by key"""
        return self.cache_data.get(key)
