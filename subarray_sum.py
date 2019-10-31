# program for calculating maximum sum of subarray

# function for subarray_sum which returns the maximum sum of contigous array
# IDEA: Logic is that we can simply initialize two varibales - current sum and maximum sum(which we have to found) and then keep iterating over the list and then, if current sum becomes negative, then make it zero because it will decrease the max sum and overall it will reinialize the current sum whereas simulataneously, keep track of maximum sum found till now by comparing it with current sum.
def subarray_sum(arr, n):
    '''
    parameters:
    arr : array/list of input integers(all)
    n : size of array
    return : returns maximum sum
    '''
    current_sum = 0
    max_sum = 0
    # iterate over the array
    for i in range(n):
        # update current sum by adding next element in the current subarray
        current_sum = max(0, current_sum + arr[i])
        # compare and set the max sum
        max_sum = max(current_sum, max_sum)
    return max_sum

# function to keep track of indices and print the subarray which contains maximum sum
def print_maximum(arr, n):
    '''
    parameters:
    arr : array/list of input integers(all)
    n : size of array
    prints the subarray containing maximum sum
    '''
    max_sum = 0
    start = 0
    end = 0
    current_sum = 0
    s = 0
    # iterating over the array
    for i in range(n):
        # calculating current sum in each iteration
        current_sum += arr[i]
        # if the current_sum is zero, so we ignore this and set the starting of subarray as just the next one index i.e. i + 1
        if current_sum < 0:
            current_sum = 0
            s = i + 1
        # if the new max_sum is found, then update it and set start index as found pointer at 's' and set this 'i' as end index as till this one we found overall max sum
        if max_sum < current_sum:
            max_sum = current_sum
            start = s
            end = i
    # printing the required subarray        
    print('subarray containing maximum sum :')
    for k in range(start, end+1):
        print(arr[k], end = " ")

# main function
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(f'max sum : {subarray_sum(arr, n)}')
    print_maximum(arr, n)
