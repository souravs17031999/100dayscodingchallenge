# Program to compute max sum for k-sized subarrays.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.

# Naive solution is to use two loops one for n times, another for n - k time, subarrays and then compute max and update max.
# It would take 0(K * N) time complexity withtou any extra space.
# Now, we will use sliding window technique to make it more optimal to 0(N)
# ---------------------------------------------------------------------------------------------------------
curr_sum, max_sum = 0, INT_MIN
for i from 0 to k - 1
    curr_sum = curr_sum + arr[i]

curr_sum => 300

for i from k to n
    curr_sum = curr_sum - arr[i - k] + arr[i]
    max_sum = max(max_sum, curr_max)

return max_sum

# ---------------------------------------------------------------------------------------------------------

# Product of all k-sized subarrays

Input: arr[] = {1, 5, 9, 8, 2, 4,
                 1, 8, 1, 2}
       k = 6
Output:   4608
The subarray is {9, 8, 2, 4, 1, 8}

Input: arr[] = {1, 5, 9, 8, 2, 4, 1, 8, 1, 2}
       k = 4
Output:   720
The subarray is {5, 9, 8, 2}

Input: arr[] = {2, 5, 8, 1, 1, 3};
       k = 3
Output:   80
The subarray is {2, 5, 8}

We can apply the same logic as before, keep sliding the window and get the current window product using last
window product.

curr_product : Product of subarray of size k beginning with arr[i]

prev_product : Product of subarray of size k beginning with arr[i-1]

curr_product = (prev_product / arr[i-1]) * arr[i + k -1]
