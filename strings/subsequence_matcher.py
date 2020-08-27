# Program to check if one string is an subsequence of other string.
# We simply move from rightmost char to leftmost char or vice-versa, by keeping two pointers to last chars of both strings.
# If both chars match, then we simply move both (decrement).
# If it doesn't match, then we simply move the pointer for second string.
# ---------------------------------------------------------------------------------------------
# TIME : 0(N), N is length of string2.

def is_subsequence(s1, s2):

    m, n = len(s1), len(s2)
    i, j = 0, 0
    while i < m and j < n:
        if s1[i] == s2[j]:
            i += 1
        j += 1


    return i == m

str1 = "gksrek"
str2 = "geeksforgeeks"

print("Yes") if is_subsequence(str1,str2) else ("No")
