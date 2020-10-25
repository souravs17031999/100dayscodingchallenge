# Program to find the maximum number of pages a student is allocated for a given n number of books and m number of students,
# such that maximum number of pages assigned to a student is minimum.
# Also, pages are arranged in ascending order and partitions are to be assinged in continuos segements.
#---------------------------------------------------------------------------------------------------------
# Ex. pages : [12, 34, 67, 90]
# m = 2
# Explain : we can allocate 2 students in three fashions:
# -> [12], [34, 67, 90]
# -> [12, 34], [67, 90]
# -> [12, 34, 67], [90]
# So, if we add up pages for each cases, minimum comes for 3rd case = 113.
#-----------------------------------------
# IDEA: Naive approach would be to actually compute all combinations of how we can allocate the books to students n(c)m-1.
# This would take up a lot of time.
# If we observe that pages are ascending order, we can use this propert to apply binary search for the identified search space.
# So, we can compute the midpoint and check if atleast this many number of pages can be allocated, then we can ignore the other search space
# and keep reducing the search spaces.
# TIME : 0(N*lg(N))
# ---------------------------------------------------------------------------------------------------------
# In depth Intuition :
# Suppose, following needs to be allocated for 2 students, 
# We need to find following : minimum allocation for max number of pages, 
# [10 | 20, 30, 40] => 90   ----
# [10, 20,| 30, 40] => 70       |-----  min(90, 70, 60) => 60
# [10, 20, 30, | 40] => 60  ----
# So, last partition is optimal and so we know that range of our answer should be between some start that is probaly, 0 but can be better 
# when we start from max element as seen above, so, we can start from last element, and then for last element of range, it can be sum of all pages of book.
# So, ans lies in (40, 100) that is in (max_element....sum_of_array)
# ---------------------------------------------------------------------------------------------------------
# In these type of questions, we need to decide how to search and based on what condition we can move to either half space.
# So, we compute "mid", and check if it is possible to allocate max that much pages, then, we move to left side of search space as we need to minimize it so there is no benefit
# in going to right side, but if it's not possible, then it means we need to move to right side as we need to increase this max allocated pages so as to fit according to 
# constraints of given number of students.
# ---------------------------------------------------------------------------------------------------------

import sys
from sys import stdin, stdout

# function to check if it's possible to allocate pages
def isPossible(arr, n, m, curr_min):
    studentUsed = 1
    pages_read = 0
    # we keep allocating pages until we run out of students count
    for i in range(n):
        if pages_read + arr[i] > curr_min:
            studentUsed += 1
            pages_read = arr[i]
            if studentUsed > m:
                return False

        else:
            pages_read += arr[i]

    return True


# function to findPages
def findPage(arr, n, m):
    sum = 0
    # if books < students, then it's not possible, because atleast one page should be allocated to one student.
    if n < m:
        return -1

    for i in range(n):
        sum += arr[i]

    # defining the search space -: start will be last element of pages, last will be overall sum of pages.
    s, e, ans = max(arr), sum, sys.maxsize

    while s <= e:
        mid = (s + e) // 2
        # mid will be our curr_min for which we check if it's possible to allocate atleast this much pages
        # if yes then we ignore right half space
        if isPossible(arr, n, m, mid):
            # we update our answer
            ans = min(ans, mid)
            e = mid - 1
        else:
            # if it's not possible
            s = mid  + 1

    return ans

# driver test function
if __name__ == '__main__':
    arr = [12, 34, 67, 90]
    n, m = 4, 2
    print(findPage(arr, n, m)) # 113
