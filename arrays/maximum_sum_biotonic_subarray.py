# Program to compute maximum sum of biotonic subarray , meaning subarray should be first increasing and
# then  decreasing.

# Logic :
# Actually, for biotonic array, in this problem, we can more than one peak, hence , and we know that first it should be increasing , then it should be decreasing, so what we can do is take two aux arrays such that first one sums up from front if and only if it is increasing (from left to right) and second one sums from behind if and only if it is decreasing (from right to left). Now, we can observe that while we construct these both arrays, we have summed up twice the element at arr[i] for every index i, hence, we need to subtract once arr[i] for each index i while computing max.
# Like in the above example : arr = [5, 3, 9, 2, 7, 6, 4]
# at index 4, we can see inc[4] = 9 (7 + 2), and dec[4] = 17 (7+6+4), so arr[4] = 7 which has been summed twice and hence we subtract 7 once, giving 19 as the answer (using msis[i] + msds[i] - arr[i]) .
# TIME : 0(N), SPACE : 0(N), N IS LENGHT OF ARRAY GIVEN.

def computeMaxBiotonic(arr):
    n = len(arr)

    inc, dec = [0] * n, [0] * n
    inc[0], dec[n - 1] = arr[0], arr[n - 1]

    # filling up increasing aux array
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc[i] = inc[i - 1] + arr[i]
        else:
            inc[i] = arr[i]

    # filling up decreasing aux array
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            dec[i] = dec[i + 1] + arr[i]
        else:
            dec[i] = arr[i]

    # computing max
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])

    return max_sum

# driver testing function
if __name__ == '__main__':
    arr = [5, 3, 9, 2, 7, 6, 4]
    print(computeMaxBiotonic(arr))
