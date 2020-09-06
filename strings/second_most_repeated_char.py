# Program for printing the second most repeated word in the given list of strings.
# Input:
# 2
# 6
# aaa bbb ccc bbb aaa  aaa
# 6
# geeks for geeks for geeks aaa
#
# Output:
# bbb
# for
# ----------------------------------------------------------------------------------------

#code
from sys import stdin, stdout

from heapq import heapify, heappop, heappush

def compute_second_repeated(arr, n):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    heap = [(-count[i], i) for i in count]
    heapify(heap)

    heappop(heap)
    return heappop(heap)[1]


if __name__ == '__main__':
    t = int(stdin.readline().strip())
    for i in range(t):
        n = int(stdin.readline().strip())
        s = stdin.readline().strip().split()
        stdout.write(compute_second_repeated(s, n))
        stdout.write('\n')
