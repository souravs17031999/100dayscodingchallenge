# Program to print the all possible permutations for a given string.
# NOTE : we can use permutations from itertools but here we do it using recursion and backtracking.
# ------------------------------------------------------------------------------------------------
# TIME : 0(N * N !)
# -----------------------------------------------------------------------------------------------
# we keep on fixing the char one by one position, and backtracking.
# First we have all chars in decision space, we fix one position and then keep going on till last decision char
# and then backtrack and do similar for next position of char.
# ------------------------------------------------------------------------------------------------
# Every time we swap the element at first position denoted by l, with the current index in the loop and then recur for remaning part of string.
# After the print of the string , we backtrack by undoing the earlier swap we did.
          #
          #
          #          A
          #       /   |  \
          #     ABC   BAC  CAB
          #   /  |     / |    | \
          # ABC  ACB  BAC BCA CAB CBA
          #

def permutate(a, l, r):

    if l == r:
        print("".join(a))

    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]  # fix this char
            permutate(a, l + 1, r)  # go for next pos
            a[l], a[i] = a[i], a[l]    # backtrack


if __name__ == '__main__':
    s = "ABC"
    permutate(list(s), 0, len(s) - 1)
