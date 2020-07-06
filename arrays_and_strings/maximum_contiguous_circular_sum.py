# Program for computing maximum contiguos sum of circular array , meaning we can compute the sum by
# warping around the array and get the maximum and return it.
# OPTIMIZED APPROACH :
# idea is here to make use of already known kadane's algorithm.
# We know that we can use kadane's algo to get the maximum sum but in the case when there is no warping.
# ALong with that the case can also occur, where there is warping and maximum is then taken from warping.
# So, how do we get maximum for warping case, for this to work, we negate the elements,
# and then apply kadane's on it, after that we basically subtract this sum from overall sum,
# resulting in sum of non contributing elements.
# This will be sum of wraped case.
# Basically, after negation, we are applying kadane on it, in this way we can get sum of non contributing elements and also we are
# taking overall sum, hence, by subtracting them we will get max sum for warped elements case.
# we can then return the maximum out of both of them.
# TIME : 0(N), SPACE : 0(1)

def maximumKadane(nums):
    curr_sum, max_sum = nums[0], nums[0]
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], nums[i] + curr_sum)
        max_sum = max(curr_sum, max_sum)
    return max_sum


def MaxCircular(arr):
    n = len(arr)
    max_kadane = maximumKadane(arr)
    wrap = 0
    for i in range(n):
        wrap += arr[i]
        arr[i] = -arr[i]

    wrap = wrap + maximumKadane(arr)

    return max(wrap, max_kadane)

if __name__ == '__main__':
    arr = [11, 10, -20, 5, -3, -5, 8, -13, 10]
    print(MaxCircular(arr))
