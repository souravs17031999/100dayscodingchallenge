# program for finding union and intersection of two arrays
# IDEA: Naive solution is to Simple check for two loops, and check if element present in one
# array is present in other or not and will take 0(N^2).
# ------------------------------------------------------------------------------------------------
# Next optimization would be to sort the array and then apply binary search to search for
# element in the sorted array against the first array and will take 0(N*lg(N)).
# OVERALL TIME : min(mLogm + nLogm, mLogn + nLogn)
# This approach works much better than the previous approach when difference between sizes of two arrays is significant.
# -------------------------------------------------------------------------------------------------
# Optimized approach :
# To convert into sets and apply union and intersection function inbuilt.
# This will take :
# Union : 0(len(s1) + len(s2))
# INtersection : 0(min(len(s1), len(s2)))
# ALSO, SPACE : 0(MAX(M, N)) WHERE M, N IS SIZE OF TWO ARRAYS.
# ------------------------------------------------------------------------------------------------
# Also, instead of using any in-built container like sets() we can write ourselves
# own hashing function and then try to search and insert using hash.
# This will also have same asymtodic bounds (if hashing function is good enough !)
# -----------------------------------------------------------------------------------------------
# What if arrays given to us are sorted ?
# Again the in-built sets will give the optimal complexity but also we can apply different approach to get linear time complexity
# for sorted arrays.
# -----------------------------------------------------------------------------------------------
# See the last approach for sorted arrays :---

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


# FOR SORTED ARRAYS :
# It is important method as it maintains order of elements.

def get_union(arr1, arr2):

    m, n = len(arr1), len(arr2)
    i, j = 0, 0
    res = set()
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            res.add(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            res.add(arr2[j])
            j += 1
        else:
            res.add(arr2[j])
            i += 1
            j += 1

    # since some of the element will be remaining and in union we want all

    while i < m:
        res.add(arr1[i])
        i += 1

    while j < n:
        res.add(arr2[j])
        j += 1

    return res

def get_intersection(arr1, arr2):

    m, n = len(arr1), len(arr2)
    i, j = 0, 0
    res = set()

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            res.add(arr2[j])
            i += 1
            j += 1

    return res


# main function
if __name__ == '__main__':
    arr1 = [random.randint(0, 10) for _ in range(10)]
    arr2 = [random.randint(0, 10) for _ in range(10)]

    # arr1.sort()
    # arr2.sort()
    # print(f"arr1 : {arr1}")
    # print(f"arr2 : {arr2}")
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 6, 7, 8]
    print(f'union is : {get_union(arr1, arr2)}')
    print(f'intersection is {get_intersection(arr1, arr2)}')
