# program to sort 0's, 1's and 2's in order

def dnf_sort(arr):
    if not len(arr):
        return []
    n = len(arr)
    count_1, count_2, count_3 = 0, 0, 0
    for i in arr:
        if i == 0:
            count_1 += 1
        elif i == 1:
            count_2 += 1
        else:
            count_3 += 1

    i = 0
    while count_1:
        arr[i] = 0
        i += 1
        count_1 -= 1

    while count_2:
        arr[i] = 1
        i += 1
        count_2 -= 1

    while count_3:
        arr[i] = 2
        i += 1
        count_3 -= 1
    return arr

if __name__ == '__main__':
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(dnf_sort(arr))
