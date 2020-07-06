# Program for computing maximum sum subarray for the given array
# ALgorithm here is Kadane's algo which takes 0(N)
# This is a variant of window sliding technique.

def maxSubArray(nums):
    curr_sum, max_sum = nums[0], nums[0]
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], nums[i] + curr_sum)
        max_sum = max(curr_sum, max_sum)
    return max_sum


if __name__ == '__main__':
    arr = [5, 3, 9, 2, 7, 6, 4]
    print(maxSubArray(arr))
