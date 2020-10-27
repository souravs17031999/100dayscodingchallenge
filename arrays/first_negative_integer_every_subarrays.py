# Program to find the first negative integer of every subarray of size "K" in the given array of size "N".
# Examples:
#
# Input : arr[] = {-8, 2, 3, -6, 10}, k = 2
# Output : -8 0 -6 -6
# First negative integer for each window of size k
# {-8, 2} = -8
# {2, 3} = 0 (does not contain a negative integer)
# {3, -6} = -6
# {-6, 10} = -6
#
# Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
# Output : -1 -1 -7 -15 -15 0 
# -------------------------------------------------------------------------------------------------------------------
# Naive solution can be to use two loops, one for outer loop to iterate the array and one for inner loop to iterate for window size of length k, 
# and maintain a flag to verify if we got any negative element earlier, if so, then print it, and get out of that inner loop, then again move to next subarray
# and also reset flag to check for next subarray , But this will be take 0(N * K) time and space  : 0(1).
# Can we do better than this ?
# Yes, if we observe, then we are doing lots of repetitive comparisons for checking if ele is -ve or not, because subarrays are overlapping, 
# and so, we need to some way to ignore these redundant comparisons, so, we can use sliding window approach so as to not check those ele in the curr window, 
# which have been already checked in the last window.
# We can actually observe this as shown below : 
# We are going to use sliding window + Deuqe based approach as we have to not only print the sinlge answr but answer for all subarrays : 
# [-8, 2, 3, -6, 10]
# maintain a deque of useful elements => those which are negative, and the first neg will be at front of deque and all other ele of curr window will be not useful for the next 
# window, therefore pop them out and append all those of new window which are negative.
# We are storing only the indices not the element as it will be useful in getting non unseful elements out of the current window.
#
# [-8, 2, 3, -6, 10] => intial array, deque : []
# now, we first go for first k elements and fill the deque with all the negative elements. 
# so, for k = 2, 
# processed, [-8, 2] => deque : [0]
#              ^  ^
# [-8, 2, 3, -6, 10] => deque : [0] , print -8
#         ^       
# [-8, 2, 3, -6, 10] => deque : []    print -8, 0 
#             ^
# [-8, 2, 3, -6, 10] => deque : [3]   print -8, 0, -6
#                 ^
# [-8, 2, 3, -6, 10] => deque : []    print -8, 0, -6, 0
#
# ----------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(K)
# Can we do better than this in space ?
#
# Yes, we have to effecively replace deque processing by a single variable because all that deque does is that it ignores all the positive elements, and take negative ele
# and print the front for every window when we start the current window.
# Now, we can also use a "first_neg" variable which can be used for skipping positive numbers.
# This can reduce the space : 0(1)
# so, TIME: 0(N), SPACE : 0(1)
# -------------------------------------------------------------------------------------------------------------------------------------------------
# DEQUE BASED APPROACH : 

from collections import deque 
def first_neg_subarray(arr, n, k):
    
    queue = deque()
    for i in range(k):
        if arr[i] < 0:
            queue.append(i)

    for i in range(k, n):
        
        if not queue:
            print(0, end = " ")
        else:
            print(arr[queue[0]], end = " ")
        
        while queue and queue[0] <= i - k:
            queue.popleft()
        
        if arr[i] < 0:
            queue.append(i)
    
    if not queue:
        print(0)
    else:
        print(arr[queue[0]])


# EXTRA VARIABLE BASED APPROACH : 
def first_neg_subarray(arr, n, k):
    
    first_neg = 0
    for i in range(k - 1, n):
        
        while first_neg < i and (first_neg <= i - k or arr[first_neg] > 0):
            first_neg += 1
        
        first_neg = arr[first_neg] if arr[first_neg] < 0 else 0
        
        print(first_neg, end = " ")

if __name__ == '__main__':
    arr = [12, -1, -7, 8, -15, 30, 16, 28] 
    n = len(arr) 
    k = 3
    first_neg_subarray(arr, n, k)  # output : -1 -1 -7 -15 -15 0

    
    
