# program for sorting positive numbers , keeping negative numbers at their place.

# importing my implementation of counting sort
from counting_sort import counting_sort as count_sort
from sys import stdin, stdout

# IDEA: logic is to move all the positive integers into a new array (list) and then sort them using counting sort and then, move them back into their
# respective position into the array by keeping a pointer at the new array and incrementing it whenever we move one element from that array to the main.
def negative_sort(arr, n):
    # moving the positive integers to the new array #for i in range(n): if arr[i] >= 0: l.append(arr[i]), same as this one.
    l = [arr[i] for i in range(n) if arr[i] >= 0]
    k = len(l)
    # sorting the array
    l = count_sort(l, k)
    p = 0
    # now, replacing the old element with the correct position of sorted element
    for i in range(n):
        if arr[i] >= 0:
            arr[i] = l[p]
            p += 1
    return arr

# main function 
if __name__ == '__main__':
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    print(negative_sort(arr, n))
