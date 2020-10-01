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

# -------------------------------------------------------------Best intution of LRU cache --------------------------------------------------------------------------------
# IMplementing LRU cache 
# LRU cache has fixed capacity (like used in OS frames - page replacement algorithms), 
# It basically means least recently used cache, when cache is full, then we delete/remove the element which
# is least recently used (not used for long time or which came very earliest), as it is likely that it will
# not be called in near future and so remove that and then move to next call.
# We need to implement two methods in 0(1):
# get(int key)
# set(int key, int value)
#
# ----------------------------------------------------------------------------------------------------------
# How do we start implementing this ?
# The naive approach could be to use nested array containing elements in the form of tuple (key, value, timestamp)
# get() : we can iterate over all the elements in the array and get the value of the key => 0(N)
# set() : we can set the value of the key at the last index if capacity is not reached, if capacity is reached
# then, we can check timestamps for all, and then remove the element with the least value of timestamp=> 0(N)
# ----------------------------------------------------------------------------------------------------------
# Can we improve on this ?
# We are going to use Doubly linked list to enable us to move in both directions, and also HashMap which can 
# enable to access the node directly in 0(1) if it's present or not.
# Also, deletion is very efficient of the node in doubly linked list and addition in front of head is also.
# So, approach will be to use Doubly linked list to actually hold the cache key-value pair, and the most 
# frequently accessed item will be pushed towards head and so eventually least recently used will be bubbled
# up to the last of the list.
# HashMap will hold <key : node address> that means now we will have direct access to the address of the node.
# ---------------------------------------------------------------------------------------------------------

# ------------------------------------------------------- IMplementing using Doubly linked list + HashMap -----------------------------------------------------------------

class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.val =  value
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity):
        
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.map = {}
    
    def delete_node(self, node):
        
        if self.head == None:
            return 
        
        if self.head.next == None:
            self.head = self.tail = None
            del node
        
        if self.tail == node:
            self.tail = node.prev
        
        node.prev.next = node.next
        node.next = node.prev
        del node
    
    def add_to_front(self, node):
        
        if self.head == None:
            self.head = self.tail = node
            return 
        
        node.next = self.head
        node.next.prev = node
        self.head = node
    
    def get(self, key):
        
        if key in self.map:
            node = self.map[key]
            value = node.val
            self.delete_node(node)
            self.add_to_front(node)
            return value
        
        print("Key not found error !")
        return -1
    
    def set(self, key, value):
        
        if key not in self.map:
            new_node = Node(key, value)
            self.map[key] = new_node
            if self.size < self.capacity:
                self.size += 1
                self.add_to_front(new_node)
            else:
                self.delete_node(self.tail)
                del self.map[key]
                self.add_to_front(new_node)
        else:
            node = self.map[key]
            node.val = value
            self.delete_node(node)
            self.add_to_front(node)
    
    def pretty_print(self):
        ptr = self.head
        while ptr:
            print(ptr.val, end = "->")
            ptr = ptr.next
        print()    
        print(self.map)  
            
if __name__ == '__main__':
    cache = LRUCache(2)
    cache.set(1, 10)
    cache.set(2, 20)
    cache.get(1)
    cache.set(3, 30)
    cache.pretty_print()
            
            
# ------------------------------------------------------- Implementation using OrderedDict ----------------------------------------------------------------------------------------------------

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
