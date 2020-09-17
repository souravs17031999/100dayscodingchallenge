# program to group same type of anagrams together
# logic is to get tuple of all the words in a list in sorted order and
# add it to the list.
# like we get tuple for one of the word : ('e', 'a', 't')
# and then other words will be appended to the same order of
# lists like "ate" will be also ('e', 'a', 't').

# -------------------------------------------------------------------------------------------
# TIME : 0(M*N*log(N))

import collections
def main(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

if __name__ == '__main__':
    l = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    main(l)
