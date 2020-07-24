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
        self.freq = 1
        self.children = {}
        self.terminal = False


class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, key):

        ptr = self.root
        for i in range(len(key)):
            ch = key[i]
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode(ch)
            else:
                ptr.children[ch].freq += 1

            ptr = ptr.children[ch]

        ptr.terminal = True

    def find_prefix(self, keys):

        for i in keys:
            self.insert(i)

        ans = []
        for i in range(len(keys)):
            ptr = self.root.children[keys[i][0]]
            temp = []
            for j in range(1, len(keys[i])):
                temp.append(ptr.data)
                if ptr.freq == 1:
                    break
                ptr = ptr.children[keys[i][j]]
            ans.append(temp)

        print(ans)

if __name__ == '__main__':

    t = Trie()
    keys = ["zebra", "dog", "duck", "dove"]
    t.find_prefix(keys)
