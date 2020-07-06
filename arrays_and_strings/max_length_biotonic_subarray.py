# Program to compute maximum sum of biotonic subarray , meaning subarray should be first increasing and
# then  decreasing.

# Logic :
# Actually, for biotonic array, in this problem, we can more than one peak, hence , and we know that first it should be increasing , then it should be decreasing, # so what we can do is take two aux arrays such that first one sums up from front if and only if it is increasing (from left to right) and second one sums from
# behind if and only if it is decreasing (from right to left). Now, we can observe that while we construct these both arrays, we have summed up twice the length at
# arr[i] for every index i, hence, we need to subtract once "1" for each index i while computing max.
# TIME : 0(N), SPACE : 0(N), N IS LENGHT OF ARRAY GIVEN.

def computeMaxBiotonic(arr):
    n = len(arr)

    inc, dec = [0] * n, [0] * n
    inc[0], dec[n - 1] = 1, 1

    # filling up increasing aux array
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc[i] = inc[i - 1] + 1
        else:
            inc[i] = 1

    # filling up decreasing aux array
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            dec[i] = dec[i + 1] + 1
        else:
            dec[i] = 1

    # computing max
    max_length = 0
    for i in range(n):
        max_length = max(max_length, inc[i] + dec[i] - 1)

    return max_length

# driver testing function
if __name__ == '__main__':
    arr = [12, 4, 78, 90, 45, 23]
    print(computeMaxBiotonic(arr))
