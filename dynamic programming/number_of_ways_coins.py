# Program for number of ways to make up to some value N.
# Dp state[value]i, where this value is sum upto that index value.
# So, we can use 1d array of size (N + 1)
# -----------------------------------------------------------------------------------------------
# TIME : 0(N * m)

def count_ways(arr, m, N):

    count = [0 for _ in range(N + 1)]

    count[0] = 1

    for i in range(1, N + 1):
        for j in range(m):
            # if we accumulate ways i, then compute for other remaining value 'i - arr[j]'
            if arr[j] <= i:
                count[i] += count[i - arr[j]]

    return count[N]

arr = [1, 5, 6]
m = len(arr)
N = 7
print("Total number of ways = ", count_ways(arr, m, N))
