# program to output product of array except self ,
# like input : [1, 2, 3, 4] , so first we leave 1, then product comes 24, then
# we leave 2, product comes 12, and so on results in [24, 12, 8, 6]

# Best solution is to identify that we can actually break the whole product into
# two parts, one that is left part of current element and one that is right
# part of current element, product of both gives overall product except self
# TIME : 0(N), SPACE : 0(N)
def product(arr):
    n = len(arr)
    output = [0]*n
    left, right = [0]*n, [0]*n
    # always first element of left product array, and last element of right
    # product array is 1, as there is nothing beyond that
    left[0], right[n-1] = 1, 1
    # filling in left product array
    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]
    # filling in right product array
    for j in range(n-2, -1, -1):
        right[j] = right[j + 1] * arr[j + 1]
    # filling in overall array
    for i in range(0, n):
        output[i] = left[i] * right[i]
    return output

# OPTIMIZING SPACE HERE, NOW 0(1)
def product1(arr):
    n = len(arr)
    output = [0]*n
    output[0] = 1
    # now we are using output array to store first left product elements
    # in itself only
    for i in range(1, n):
        output[i] = output[i-1] * arr[i-1]
    # no use of right product array instead we use a variable to keep track of
    # of it and calculate it on the fly and then put overall product in the
    # output array itself
    right = 1
    for i in range(n-1, -1, -1):
        output[i] = output[i] * right
        right *= arr[i]
    return output

# main driver function 
if __name__ == '__main__':
    print(product1([1, 2, 3, 4]) == [24, 12, 8, 6])
    print(product1([1, 7, 3, 2, 5]) == [210, 30, 70, 105, 42])
