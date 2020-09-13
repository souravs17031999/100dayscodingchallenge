# Program for computing median of sliding k-sized window in the array.
# Input is array of integer arr[] and an integer K, we need to find the median of each window of size K
# starting from left and moving towards the right by one position each time.

# Input: arr[] = {-1, 5, 13, 8, 2, 3, 3, 1}, k = 3
# Output: 5 8 8 3 3 3
#
# Input: arr[] = {-1, 5, 13, 8, 2, 3, 3, 1}, k = 4
# Output: 6.5 6.5 5.5 3.0 2.5

# -------------------------------------------------------------------------------------------------------------------
# Naive Approach:
# The simplest approach to solve the problem is to traverse over every window of size K and sort the elements of
# the window and find the middle element. Print the middle element of every window as the median.
# Time Complexity: O(N*KlogK)
# Auxiliary Space: O(K)

# This is different than median in a stream where we use heaps - one min heap and one max heap.

# This can be solved using GNU-policy based data structures in C++ or Treeset in Java.

# In python, we can use sortedcontainers for sortedlist.
