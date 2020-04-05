# program to move all the zeros to the end of the array and all non zero elements in front of the array
# while maintaining their relative order

def fun(arr):
    n = len(arr)
    ptr = 0
    for i in range(0, n):
        if arr[i] != 0:
            arr[ptr] = arr[i]
            ptr += 1

    for i in range(ptr, n):
        arr[i] = 0

    return arr

if __name__ == '__main__':
    assert fun([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert fun([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert fun([0, 0, 0, 0, 12]) == [12, 0, 0, 0, 0]
    assert fun([]) == []
    assert fun([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
