#!/usr/bin/env python3
"""
caching implementation
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Least-frequently used (LFU) caching
    """
    frecuency_dict = {}

    def __init__(self):
        """
        Class initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key
        """
        if key is None or item is None:
            return

        frecuency = self.frecuency_dict.get(key, 0)
        if key in self.cache_data:
            del self.frecuency_dict[key]
            del self.cache_data[key]
        self.frecuency_dict[key] = frecuency + 1
        self.cache_data[key] = item

        if len(self.cache_data) <= BaseCaching.MAX_ITEMS:
            return

        for k in sorted(self.frecuency_dict, key=self.frecuency_dict.get):
            if k != key:
                discard = k
                del self.cache_data[k]
                print(f"DISCARD: {discard}")
                del self.frecuency_dict[k]
                break

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        item = self.cache_data.get(key)
        if item:
            del self.cache_data[key]
            self.cache_data[key] = item

            frecuency = self.frecuency_dict.get(key)
            del self.frecuency_dict[key]
            self.frecuency_dict[key] = frecuency + 1

        return item
