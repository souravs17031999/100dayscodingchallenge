# program to generate wave type of sort known as wave sort, which satisfies following condition :
# arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..
# IDEA: Logic is to fix all the even indices such that it gets bigger than its either adjacent elements (both sides) except first and last,
# the way to do is to traverse over the array and check if current even index element is smaller than previous one, then swap these both and
# similarly if it is smaller than its next element then, swap those, all other elements are taken care of.
# Time : 0(N), space: 0(1)

# function for sorting the array in wave form : B-S-B-S-B....
def wave_sort(arr):
    n = len(arr)
    for i in range(0, n, 2):

        if i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        if i < n - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr

if __name__ == '__main__':
    assert wave_sort(arr = [1, 3, 4, 2, 7, 5]) == [3, 1, 4, 2, 7, 5]
    assert wave_sort(arr = [10, 90, 49, 2, 1, 5, 23]) == [90, 10, 49, 1, 5, 2, 23]
