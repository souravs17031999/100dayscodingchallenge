# Program to find the most occuring word in the given string array.
# If same frequency, then print in order of input (last string having max same frequency should be printed)
# EX.
# Input:
# 3
# 3
# geeks for geeks
# 2
# hello world
# 3
# world wide fund
#
# Output:
# geeks
# world
# fund
# --------------------------------------------------------------------------------------------------------

from sys import stdin, stdout
import sys
from collections import OrderedDict

def count_max_freq(arr, n):

    count = OrderedDict()
    for i in range(n):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1

    max_ele, max_idx = None, 0

    for i, j in count.items():
        if j >= max_idx:
            max_idx = j
            max_ele = i

    return max_ele

if __name__ == '__main__':
    print(count_max_freq(['world', 'wide', 'fund'], 3))
