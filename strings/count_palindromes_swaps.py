# Program to compute possible count of palindrome after swapping the chars each at a time.
# ----------------------------------------------------------------------------
# s = "abba", 1st swap : zeroth and third index swaps, "abba" => palindrome
# 2nd swap : "abba" : first index and third index, "abba" => palindrome
# other swaps, like zeroth and first index, abba => baba which is not palindrome
# and similarly all other are not palindrome.
# s = "aaabaaa"
# Naive approach would be to generate all possible pairs for swapping and then check
# if after swapping, if it is palindrome or not.
# Generating possible pairs would be 0(N^2), and checking palindrome would be all
# in 0(N^3) time.
# ----------------------------------------------------------------------------
# Can we do better than this ?
# So, logic is that only same number of characters can be swapped, and then we can
# simply count this swaps by counting the times (frequecny) when we see it.
# For the first time we see it , it is not taken into account, but when we see it
# again, then it means a swap is possible, so we increment the count like this .
# -----------------------------------------------------------------------------
# NOTE : given input consists only of lower case ascii letters.
# TIME : 0(N), SPACE : 0(N), N is length of string.

def compute_swaps_palindromes(s):

    count = [0] * 26
    res = 0
    for i in range(len(s)):
        res += count[ord(s[i]) - ord('a')]
        count[ord(s[i]) - ord('a')] += 1

    return res

if __name__ == '__main__':
    assert compute_swaps_palindromes("abba") == 2
    assert compute_swaps_palindromes("aaabaaa") == 15
