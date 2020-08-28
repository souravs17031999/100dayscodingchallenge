# Program for checking if the strings given are scrambled or not.
# Defining scrambled : if we construct binary tree then, swapping nonleaf nodes will produce another scrambled string.
# We are not allowed to break into either side empty string.
# EX.
#
#     coder
#    /    \
#   co    der
#  / \    /  \
# c   o  d   er
#            / \
#           e   r
#
# Here, we swap "o" and "c".
#
#     ocder
#    /    \
#   oc    der
#  / \    /  \
# o   c  d   er
#            / \
#           e   r
#
# “ocder” is a scrambled string of “coder”
# Similarly other swaps can be done and more scrambled forms can be construced.
#
# Now, if we observe carefully, then we can basically break down this tree at different break points taking from i = 1 to n - 1
# (as empty string is not allowed)
# So, this hints at this problem being kind of variation of MCM.
# Approach : logic is to understand that for every point i, there are two cases => either there is swap or there is not swap.
# So, if there is a swap :
# let's say ex.: for i = 2, "gr|eat" => eat|gr
# Then, we need to recursively check "first two of great" and "last two of eatgr" and Similarly "last three of great" and "first three of eatgr"
# But if there is no swap : "gr|eat" => "gr|eat"
# Then, we need to check "first two of both" and "last three of both".
# So, either of these if returned True, then we can safely return True.
# ---------------------------------------------------------------------------------------------------------------------

# simple recursion

def is_scrambled(s1, s2):

    if len(s1) != len(s2):
        return False

    if not len(s1) and not len(s2):
        return True

    if s1 == s2:
        return True

    if len(s1) <= 1:
        return False

    n = len(s1)
    flag = False

    for i in range(1, n):
        # first condition is for swap occured and second condition is for no swap occured
        if (is_scrambled(s1[:i], s2[n-i:]) and is_scrambled(s1[i:], s2[:n-i])) or (is_scrambled(s1[:i], s2[:i]) and is_scrambled(s1[i:], s2[i:])):
            flag = True
            break

    return flag

# TOPDOWN MEMOIZED

cache = {}

def is_scrambled_memo(s1, s2):

    if len(s1) != len(s2):
        return False

    if not len(s1) and not len(s2):
        return True

    if s1 == s2:
        return True

    if len(s1) <= 1:
        return False

    if (s1, s2) in cache:
        return cache[(s1, s2)]

    n = len(s1)
    flag = False

    for i in range(1, n):
        # first condition is for swap occured and second condition is for no swap occured
        if (is_scrambled_memo(s1[:i], s2[n-i:]) and is_scrambled_memo(s1[i:], s2[:n-i])) or (is_scrambled_memo(s1[:i], s2[:i]) and is_scrambled_memo(s1[i:], s2[i:])):
            flag = True
            break

    cache[(s1, s2)] = flag
    return flag

print(is_scrambled("coder", "ocder"))
print(is_scrambled("abcde", "caebd"))
print(is_scrambled_memo("coder", "ocder"))
print(is_scrambled_memo("abcde", "caebd"))
