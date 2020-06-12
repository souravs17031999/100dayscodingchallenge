# program for finding union and intersection of two arrays (sets)

from sys import stdin, stdout
# function for binary search
def binary_search(arr, start, end, key):
    while(start <= end):
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return 1
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

# function for union of sets (arrays)
# IDEA: logic is that we can linearly scan one of the array and then apply binary search for second one by first sorting it, and then taking one of the arrays including already the elements which are present in that , along with the newly appended which were there in second array but not in current one will modify the original array and return it.
def union(arr1, arr2):
    arr2.sort()
    for i in range(len(arr1)):
        if(not binary_search(arr2, 0, len(arr2)- 1, arr1[i])):
            arr2.append(arr1[i])
    arr2.sort()
    return arr2

# function for intersection of sets (arrays)
# IDEA: logic is almost same as union except that here now, we are interested in those elements which are there in both arrays so, we create a temporary array and add those which are there in both arrays.
def intersection(arr1, arr2):
    l = []
    for i in range(len(arr1)):
        if(binary_search(arr2, 0, len(arr2)- 1, arr1[i])):
            l.append(arr1[i])
    l.sort()
    return l

# main function 
if __name__ == '__main__':
    n1 = int(stdin.readline().strip())
    n2 = int(stdin.readline().strip())
    arr1 = list(map(int, stdin.readline().strip().split()))
    arr2 = list(map(int, stdin.readline().strip().split()))
    arr1_copy, arr2_copy = arr1.copy(), arr2.copy()
    print(f'union is : {union(arr1, arr2)}')
    print(f'intersection is {intersection(arr1_copy, arr2_copy)}')
