# Program to print all the unique prefix shortest possible for the list of strings
# Input: arr[] = {"zebra", "dog", "duck", "dove"}
# Output: dog, dov, du, z
# IDEA: Naive approach will be inefficient as we have to check every possible prefix in all the words,
# in every word possible in the list given as input.
# It will be somewhat approaching : 0(N * M), where N is sum of all chars in the overall strings,
# and M is length of list given as input.
# OPTIMISED APPROACH :
# Trie, Will be an very effient approach, as If we insert all the strings into trie as keys,
# Then, we will be able to it in 0(N) time.
# While inserting keys, we have to also keep a count of frequency along with the data.
# While traversing, once we reach first node where freq == 1, then at that point,
# we can print for that string.

class TrieNode:

    def __init__(self, data):
        self.data = data
        self.children = [0] * 256 # can also use 26 , ord(ch) - ord('a')
        self.freq = 1
        self.terminal = False


class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def index(self, ch):
        return ord(ch)

    def insert(self, key):

        ptr = self.root
        for i in range(len(key)):
            ch = key[i]
            index = self.index(ch)
            if not ptr.children[index]:
                ptr.children[index] = TrieNode(ch)
            else:
                ptr.freq += 1

            ptr = ptr.children[index]

        ptr.terminal = True


    def pretty_print(self, keys):

        for i in range(len(keys)):
            ch = keys[i][0]
            index = self.index(ch)
            ptr = self.root.children[index]
            print(f"{ptr.data} ({ptr.freq}) ", end = "")
            for j in range(len(keys[i])):
                ch_index = self.index(keys[i][j])
                if ptr.children[ch_index]:
                    ptr = ptr.children[ch_index]
                    print(f"{ptr.data} ({ptr.freq}) ", end = "")
            print()

    def find_prefix(self, keys):

        for i in keys:
            self.insert(i)

        ans = []
        for i in range(len(keys)):
            ptr = self.root.children[self.index(keys[i][0])]
            temp = []
            for j in range(1, len(keys[i])):
                temp.append(ptr.data)
                if ptr.freq == 1:
                    break
                ptr = ptr.children[self.index(keys[i][j])]
            ans.append(temp)

        print(ans)

if __name__ == '__main__':

    t = Trie()
    keys = ["zebra", "dog", "duck", "dove"]
    t.find_prefix(keys)
    t.pretty_print(keys)
