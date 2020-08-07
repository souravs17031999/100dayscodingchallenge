# LRU cache algorithm is least recently used algorithm used to remove least recently used item from cache
# So, we need to keep a track of least recently used items and also maintain a map
# for mapping page numbers to frames.
# Since, cache size is fixed and some positive value , this can be thought of as
# no. of frames available (which is generally fixed).
# Overall, we need to use some kind of data structure which is keeping ordering among
# the inserted items.
# Here, we can use a Queue using doubly linked list and HashTable for fast lookups.
# Hashtables will help in directly locating the value in the list (stores node address).
# So, for performance, we are using OrderedDict
# --------------------------------------------------------------------------------
# Let's say we have a reference string , each of which CPU is asking for page no.
# 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
# Now, considering we have 3 frames in the main memory :
#     3
#   2 2
# 1 1 1 now, when we want to insert new item "4" in frames, then we need to remove
# least recently used that is "1", and insert "4".
#      3   3
#   2  2   2
# 1 1  1   4 and in this way we can acheive.
# --------------------------------------------------------------------------------
# TIME : 0(1)

from collections import OrderedDict
class LRU:

    def __init__(self, size):

        self.cache = OrderedDict()
        self.capacity = size

    def get(self, key):

        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):

        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def pretty_print(self):

        print(self.cache)

if __name__ == '__main__':

    cache = LRU(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    print(cache.get(2))
    cache.pretty_print()
