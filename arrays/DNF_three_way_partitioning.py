# Program for three way Partitioning, such that the overall array is paritioned into three
# paritions such that elements shorter than pivot (mid) will be before the pivot,
# and elements greater than pivot will be greater than pivot.
# In this way, we will be having three regions, such that there will be elements lesser than
# pivot, some elements equal to pivot region and then elements greater than pivot.
# TIME : 0(N), SPACE : 0(1).

import random
def Partition(arr, mid):
    i, j, k = 0, 0, len(arr)
    while j < k:
        if arr[j] < mid:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > mid:
            k -= 1
            arr[j], arr[k] = arr[k], arr[j]
        else:
            j += 1

if __name__ == '__main__':
    arr = [random.randint(0, 2) for _ in range(10)]
    print(arr)
    Partition(arr, 1)
    print(arr)
