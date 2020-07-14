# program for finding union and intersection of two arrays
# IDEA: Naive solution is to Simple check for two loops, and check if element present in one
# array is present in other or not and will take 0(N^2).
# Next optimization would be to sort the array and then apply binary search to search for
# element in the sorted array against the first array and will take 0(N*lg(N)).
# Optimized approach :
# To convert into sets and apply union and intersection function inbuilt.
# This will take :
# Union : 0(len(s1) + len(s2))
# INtersection : 0(min(len(s1), len(s2)))
# ALSO, SPACE : 0(MAX(M, N)) WHERE M, N IS SIZE OF TWO ARRAYS.
# Also, instead of using any in-built container like sets() we can write ourselves
# own hashing function and then try to search and insert using hash.
# This will also have same asymtodic bounds (if hashing function is good enough !)

from sys import stdin, stdout
import random

def compute_union(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.union(set2))

def compute_intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))

# function for binary search
# def binary_search(arr, start, end, key):
#     while(start <= end):
#         mid = start + (end - start) // 2
#         if arr[mid] == key:
#             return 1
#         if key < arr[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return 0
#
# # function for union of sets (arrays)
# # IDEA: logic is that we can linearly scan one of the array and then apply binary search for second one by first sorting it, and then taking one of the arrays including already the elements which are present in that , along with the newly appended which were there in second array but not in current one will modify the original array and return it.
# def union(arr1, arr2):
#     arr2.sort()
#     for i in range(len(arr1)):
#         if(not binary_search(arr2, 0, len(arr2)- 1, arr1[i])):
#             arr2.append(arr1[i])
#     arr2.sort()
#     return arr2
#
# # function for intersection of sets (arrays)
# # IDEA: logic is almost same as union except that here now, we are interested in those elements which are there in both arrays so, we create a temporary array and add those which are there in both arrays.
# def intersection(arr1, arr2):
#     l = []
#     for i in range(len(arr1)):
#         if(binary_search(arr2, 0, len(arr2)- 1, arr1[i])):
#             l.append(arr1[i])
#     l.sort()
#     return l

# main function
if __name__ == '__main__':
    arr1 = [random.randint(0, 10) for _ in range(10)]
    arr2 = [random.randint(0, 10) for _ in range(10)]
    print(f"arr1 : {arr1}")
    print(f"arr2 : {arr2}")
    print(f'union is : {compute_union(arr1, arr2)}')
    print(f'intersection is {compute_intersection(arr1, arr2)}')
