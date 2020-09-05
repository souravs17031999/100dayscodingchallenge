# Program for computing the longest common prefix of the given list of strings.
# EX.
# INPUT : list of strings : ['geeksforgeeks', 'geeks', 'geek', 'geezer']
# OUTPUT : ['gee']
# INPUT : list of strings : ['apple', 'ape', 'april']
# OUTPUT : ['ap']
# ---------------------------------------------------------------------------------------------------------------
# There are various approaches for solving this problem :
# Firstly, we can match word by word for common prefix by counting the chars of both strings and get the longest match for
# each two strings one by one.
# TIME : 0(N * Length of maximum string), N is total number of strings
# --------------------------------------------------------------------------------------------------
# Next, we can improve this by going for char by char.
# We can actually, visualize this and have all the pointers to all the strings and match it one by one
# and count it until either one of the string gets exhausted or one of them don't match.
# TIME : 0(N * LENGTH OF maximum STRING MACTHED).
# It's more practical approach in overall runtimes.
# -----------------------------------------------------------------------------------------------------------------
# THird approach that is more intuitive and applicable here, would be using Trie though with same asymtodic bounds.
# class TrieNode: with same as usual components.
# Now, while marking new nodes everythime , initilize it with word_count as 1, and while going through it again increment.
# Now, after making Trie, we can again go through root node and append all the characters till the node which contains word contain < total strings.
# ----------------------------------------------------------------------------------------------------------------
# Fourth approach could be to sort all the strings.
# Now, simply first and last string and whatever string matches then we can return the result.
# TIME : N * LOG(N)
# -------------------------------------------------------------------------------------------------------------------
# Fifth approach : Divide and conquer approach, we can keep dividing the array of strings and compute lcp for them, base case being only one string.
# Sixth approach : Using binary search


# METHOD 1............

def common_prefix(s1, s2):

    result = []
    s1_ptr, s2_ptr = 0, 0
    while s1_ptr < len(s1) and s2_ptr < len(s2):

        if s1[s1_ptr] != s2[s2_ptr]:
            break

        result.append(s1[s1_ptr])
        s1_ptr += 1
        s2_ptr += 1

    return "".join(result)

def lcp_word_by_word(arr, n):

    prefix = arr[0]
    count = [0]
    for i in range(1, n):
        prefix = common_prefix(prefix, arr[i])

    return prefix

# METHOD 2......................
import sys
def lcp_char_by_char(arr, n):
    min_length = sys.maxsize
    for i in range(n):
        min_length = min(min_length, len(arr[i]))

    res = []
    for i in range(min_length):

        curr = arr[0][i]
        for j in range(1, n):
            if arr[j][i] != curr:
                return "".join(res)

        res.append(curr)

    return "".join(res)

# METHOD 4 :

def lcp_word_by_word(arr, n):

    arr.sort()
    return common_prefix(arr[0], arr[-1])


# METHOD 5 : (Divide and conquer approach , similar to method 1)

def lcp_divide_conquer(arr, low, high):

    if low == high:
        return arr[low]

    if low < high:

        mid = low + (high  - low) // 2
        s1 = lcp_divide_conquer(arr, low, mid)
        s2 = lcp_divide_conquer(arr, mid + 1, high)

        return common_prefix(s1, s2)

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
n = len(arr)
print(lcp_word_by_word(arr, n))
print(lcp_char_by_char(arr, n))
arr = ['apple', 'ape', 'april']
n = len(arr)
print(lcp_divide_conquer(arr, 0, n - 1))
