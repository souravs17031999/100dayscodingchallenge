import random
def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

if __name__ == '__main__':
    insertion_sort([random.randint(1, 100) for x in range(100)])
