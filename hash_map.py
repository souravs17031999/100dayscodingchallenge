class hashmap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def get_hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.size

    def add(self, key, value):
        index = self.get_hash(key)
        if self.map[index] == None:
            self.map[index] = [key, value]
        else:
            for pair in self.map[index]:
                if pair != None:
                    if pair[0] == key:
                        return pair    
            self.map[index].append([key, value])

    def get_value(self, key):
        index = self.get_hash(key)
        if self.map[index] == None:
            print('Key error')
        else:
            for pair in self.map[index]:
                if pair != None:
                    if pair[0] == key:
                        return pair

    def delete(self, key):
        index = self.get_hash(key)
        if self.map[index] == None:
            print('key error')
        else:
            self.map[index] = None

    def print_hashmap(self):
        print(self.map)

if __name__ == '__main__':
    h = hashmap(6)
    h.add('sourav kumar', 100)
    h.add('elon musk', 95)
    h.add('jennifer lawrence', 98)
    h.add('sourav kumar', 120)
    h.print_hashmap()
