# Program to return the longest possible palindrome substring in a given string with its maximum length
# Logic is to start at the middle of string and expand around center in both directions and
# keeping track of maximum length so far and return the maximum for all sets of chars of string starting
# from that char, so there will be two cases - even length palindromes and odd length palindromes but both will be handled
# as in case of odd length we will choose our start and end pointer for expanding around center as the same char, but for the
# case of even length palindrome, we will choose start as something and just next one as end , so all will be covered like this.
# Time : 0(N*N) , Space : 0(1)

# Function for generating length of palindrome for the given different sets of substrings
def length_palindrome(s, start, end):
    if s == None or start > end:
        return 0
    n = len(s)
    # keep moving start pointer left and end pointer right , 
    # until all matches are made 
    while start >= 0 and end < n and s[start] == s[end]:
        start -= 1
        end += 1
    # returning the length of current palindromic substring found
    return end - start - 1

# function for generating longest substrings of all possible substrings
def longest_palindrome(s):
    n = len(s)
    if s == None or n == 0:
        return ""
    max_length = 0
    cur_max = 0
    start, end = 0, 0
    for i in range(0, n):
        # for handling odd length palindromes 
        l1 = length_palindrome(s, i, i)
        # fkr handling even length palindromes
        l2 = length_palindrome(s, i, i + 1)
        # anyone one of them could be longer so making track of that
        cur_max = max(l1, l2)
        # keeping track of overall length maximum found so far
        max_length = max(max_length, cur_max)
        # we can stop here if we are just required to find length
        # but this is needed as we need to print the substring
        # so for that we need both start and end pointers (indices of chars)
        if cur_max > end - start:
            start = i - ((cur_max - 1) // 2)
            end = i + (cur_max // 2)
    print(s[start : end + 1])
    return max_length

if __name__ == '__main__':
    assert longest_palindrome("racecar") == 7
    assert longest_palindrome("abba") == 4
    assert longest_palindrome("forgeeksskeegfor") == 10
    assert longest_palindrome("bbbab") == 4
