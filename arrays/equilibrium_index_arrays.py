# Program for computing equilibrium index for the array if it exists.
# Array may contain positive, negative and zero values.
# Equilibrium index is the point from where sum of all left elements,
# and sum of all right elements are same.
# -------------------------------------------------------------------------------
# Now, Naive solution would be to simply for every index, compute left sum and right sum and compare,
# but that would take 0(N^2).
# -------------------------------------------------------------------------------
# Can we do better ?
# Yes, we can do it in one linear scan by using following approach.
# Let's say we compute the sum of the array in linear time, and now set this as right sum.
# As we can compute left sum as we go through the array left to right, the only problem was in right sum
# and now we already have total sum, so we can simply subtract the current element value from total sum and keep
# updating it.
# In this way, at every index, we can have left sum as well as value of right sum and simply compare whether they are equal.
# Time : 0(N), space : 0(1)
# ---------------------------------------------------------------------------------

def compute_equilibrium_index(arr, n):

    right_sum = sum(arr)
    left_sum = 0
    for i in range(n):

        right_sum -= arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
print ('First equilibrium index is ', compute_equilibrium_index(arr, 7))        
