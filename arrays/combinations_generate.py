arr = [1, 2, 3, 4, 5]

def combinations(arr, n, r, index, temp, i):
    
    if index == r:
        print(temp)
        return
    
    if i >= n:
        return
    
    temp[index] = arr[i]
    combinations(arr, n, r, index + 1, temp, i + 1)
    combinations(arr, n, r, index, temp, i + 1)

temp = [0] * 3
combinations(arr, 5, 3, 0, temp, 0)
