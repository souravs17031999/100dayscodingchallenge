# This is similar to another hashmap design problem, it's just that, here we don't handle collisions
# Also, we are given any prefixed size, so we are simply assuming size,
# This can be good question to ask or to assume (after asking interviewer) during the interview.

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10
        self.map = [None] * self.size

    def get_hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = self.get_hash(key)
        if self.map[index] == None:
            self.map[index] = list([key, value])
        else:
            self.map[index] = list([key, value])


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.get_hash(key)
        if self.map[index] == None:
            return -1
        else:
            return self.map[index][1]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.get_hash(key)
        if self.map[index] == None:
            return -1
        else:
            self.map[index] = None

    def pretty_print(self):
        print(self.map)


if __name__ == '__main__':
#    Your MyHashMap object will be instantiated and called as such:
    hashMap = MyHashMap();
    hashMap.put(1, 1);
    hashMap.put(2, 2);
    print(hashMap.get(1))
    print(hashMap.get(3))
    hashMap.put(2, 1);
    print(hashMap.get(2))
    hashMap.remove(2);
    print(hashMap.get(2))
