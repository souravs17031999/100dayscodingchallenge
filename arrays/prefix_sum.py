# program to create prefix sum array array prefixSum[] of same size such that the value of prefixSum[i] is arr[0] + arr[1] + arr[2] … arr[i].

def prefix_sum(arr):
    if len(arr) == 0:
        return
    if len(arr) == 1:
        return [arr[0]]
    arr_size = len(arr)
    prefix_array = [0] * arr_size
    prefix_array[0] = arr[0]
    for i in range(1, arr_size):
        prefix_array[i] = arr[i] + prefix_array[i - 1]
    return prefix_array

# main function
if __name__ == '__main__':
    prefix_sum([10, 20, 10, 5, 15]) == [10, 30, 40, 45, 60]
    prefix_sum([10, 4, 16, 20 ]) == [10, 14, 30, 50]
    prefix_sum([]) == None
    prefix_sum([10]) == [10]
