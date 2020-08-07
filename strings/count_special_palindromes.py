# Program to find count of special palindromes such that following conditions met :
# * A Substring is called special palindromic substring if all the characters in the
# substring are same.
# * only the middle character is different for odd length.
# We need to return the all counts of such that at least any one of the conditions met.
# ---------------------------------------------------------------------------------------
# EX. "aabbb" => "aa", "bb", "bbb", "bb"
# So, we can see "aa" contains all same chars, same with "bb", "bbb", "bb"
# EX. "abab" => "aba", "bab".
# Now, we can think "aba" contains "b" containing same char "a" on either side.
# --------------------------------------------------------------------------------------
# Naive solution is to generate all the possible pairs for the string and check if one of
# the condition is met.
# This would take 0(N^3).
# ----------------------------------------------------------------------------------------
# Can we do better ?
# We observe that we can actually compute this problem in two parts and combining two
# solutions for both parts,
# CASE 1: when all are same chars,
# so, we know when we find that max. length which are same chars, then we can find total
# possible substrings for that length k, is k * (k + 1) // 2.
# CASE 2: When around the center, all are same either side (for odd length).
# So, we can expand either side by keeping pointer at the center, starting from 1st index.
# And we can count all the possible till there is no same either side chars.
# All of the two cases for every string char iterating.
# ----------------------------------------------------------------------------------------
# This can be done in 0(N).
# -------------------------------------------------------------------------------------

def count_special_pal(s):
    n = len(s)
    ans = n
    for i in range(n):

        repeat = 0
        while i + 1 < n and s[i] == s[i + 1]:
            repeat += 1
            i += 1
        ans += repeat * (repeat + 1) // 2

        ptr = 1
        while i - ptr >= 0 and i + ptr < n and s[i + ptr] == s[i - 1] and s[i - ptr] == s[i - 1]:
            ans += 1
            ptr += 1

    return ans

if __name__ == '__main__':
    assert count_special_pal("aabbb") == 4
    assert count_special_pal("abab") == 2
