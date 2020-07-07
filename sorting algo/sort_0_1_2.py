# Program to efficietly sort the array containing only 0's, 1's, 2's.
# We simply take two variables and in one pass count all the 0's and 1's.
# Then, already we have size, so we know size - (count1 + count2) will be count for 2's.
# Now, we copy in the array directly one by one that many number of times stored in count1, count2 and size - (count1 + count2).

def sort_linear(arr, n):
    count1, count2 = 0, 0
    for i in arr:
        if i == 0:
            count1 += 1
        elif i == 1:
            count2 += 1

    k = 0
    for i in range(count1):
        arr[k] = 0
        k += 1

    for i in range(count2):
        arr[k] = 1
        k += 1

    for i in range(n - (count1 + count2)):
        arr[k] = 2
        k += 1


if __name__ == '__main__':
    arr = [0, 1, 2, 1, 2]
    sort_linear(arr, 5)
    print(arr)
