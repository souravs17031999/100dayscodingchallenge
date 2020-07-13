# Program for arranging the array, so that we get the biggest number possible.
## IDEA: logic is to sort these numbers but using custom comparator function.
# Custom comparator function will be such that it will take two arguments - X, Y and we compare XY (Y appended at the end of X),
# YX (X appended at the end of Y).
# If XY is larger, X should come before in output, else Y should come before.
# EX. X,Y = > 542, 60
# X -> 54260, Y-> 60542, SINCE 60542 IS GREATER, THEN WE PUT Y FIRST.

import functools

def Compare(x, y):
    return ((int(f"{y}{x}") > int(f"{x}{y}")) - (int(f"{y}{x}") < int(f"{x}{y}")))

if __name__ == '__main__':
    arr = [54, 546, 548, 60]
    arr.sort(key=functools.cmp_to_key(Compare))
    print("".join(list(map(str, arr))))
