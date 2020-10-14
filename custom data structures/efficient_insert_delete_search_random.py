# Program for efficiently performing following operations in 0(1) {theta} time.
# -------------------------------------------------------------------------
# insert(x): Inserts an item x to the data structure if not already present.
# remove(x): Removes an item x from the data structure if present.
# search(x): Searches an item x in the data structure.
# getRandom(): Returns a random element from current set of elements
# --------------------------------------------------------------------------
# insert(), remove() and search() can be done using hashtable in 0(1) time but getRandom can't be done as there is no ordering in the
# hashtable and so we need to get some kind of array so, we will use resizable array (list/vector) to get theta(1) time complexity.
# --------------------------------------------------------------------------

import random
class Get_Random_Interface:

    def __init__(self):
        self.map = {}
        self.arr = []
        self.size = 0

    def insert(self, x):
        if x in self.map:
            print("already exists !")
            return

        self.map[x] = self.size
        self.arr.append(x)
        self.size += 1

    def remove(self, x):
        if x not in self.map:
            print("Doesn't exist !")
            return

        idx = self.map[x]
        self.arr[idx], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[idx]
        self.arr.pop()
        del self.map[x]
        self.size -= 1

    def search(self, x):
        if x not in self.map:
            print("Doesn't exist !")
            return

        return self.map[x]

    def getRandom(self, x):
        r_idx = random.randrange(0, self.size)
        return self.arr[r_idx]

    def pretty_print(self):
        print(self.arr)
        print(self.map)

# test driver method for custom ds 
# -------------------------------------------------
if __name__ == '__main__':
    ds = Get_Random_Interface()
    ds.insert(1)
    ds.insert(2)
    ds.insert(3)
    ds.remove(2)
    ds.insert(5)
    ds.remove(10)
    print(ds.search(5))
    ds.pretty_print()
