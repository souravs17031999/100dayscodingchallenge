import random
def counting_sort(arr, exp):
    d = 10 # since we know only 0-9 digits can be possible at any nth place of digit
    output = [0 for _ in range(len(arr))]
    count = [0 for _ in range(d)]
    for i in range(len(arr)):
        index = arr[i] // exp  # this extracts the required part of digit
        count[index % 10] += 1 # index % 10 retreives last digit

    for i in range(1, d):
        count[i] += count[i - 1]

    for i in range(len(arr)-1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # we go for dividing and taking modulus starting from 1, 10, 100, 1000 till we hit 0
    exp = 1
    m = max(arr)
    while m/exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

if __name__ == '__main__':
    arr = [random.randint(0, 10000) for _ in range(10)]
    print(f"unsorted array : {arr}")
    print(f"sorted array  : {radix_sort(arr)}")
