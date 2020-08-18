# Program to compute maximum of all subarrays of given size "K" .
# IDEA: Logic is to create and maintain deque for having useful elements only in the current window that is maximum elements
# We will be maintaining the deque such that first index will always store the max element and last index will always store the min element
# Now, first we process the first k elements, then we for remaining elements, and we remove all the elements that are not of this current window and
# then , find out maximum and insert into the deque.
# In this way, TIME : 0(N),  SPACE : 0(KS)

from collections import deque

# function to compute maximum from the array of given size k
def compute_maximum(arr, k):
    # length of array in 0(N)
    n = len(arr)
    # intializing deque
    q = deque()

    # process first k elements such that [1, 2, 3....] => stores only 3 in deque but if like [1, 3, 2....] so
    # we have to store both 3, 2 both in deque because maybe in next iteration 2., 0, -1... so 2 is required
    for i in range(k):
        # this loop will run until we found first min element, so we will stop at the maximum found so far
        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        # we insert the maximum found for first k elements
        q.append(i)

    # process remaining elements
    for i in range(k, n):

        # print the max
        print(arr[q[0]], end = " ")

        # this will remove all the elements that are out of the current window (contraction)
        while q and q[0] <= i - k:
            q.popleft()

        # this loop will again run until it hits the first min element, so we will stop at the maximum found so far
        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        # insert the maximum for the current window (expansion)
        q.append(i)

    # maximum for the last window
    print(arr[q[0]])

# driver testing function
if __name__ == '__main__':
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    compute_maximum(arr, k)   # 78 90 90 90 89
