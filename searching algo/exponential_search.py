# Program to search the element using exponential search algorithm
# IDEA: logic of the algorithm is to use the fact that if we are able to find the bounds of the answer where it may lie
# and then using binary search algorithm because that range is already ordered, and we just need to check our answer (if it actually exists)
# TIME : 0(lg(i)) where i is the index of the element to be existence (if it is in the list), assuming the list is already sorted (in comparison to binary
# search , it is much faster especially in case if the key is near to the first element)


def binary_search(l, start, end, key):
    while(start <= end):
        middle = (start + end) // 2
        if key < l[middle]:
            end = middle - 1
        elif key > l[middle]:
            start = middle + 1
        else:
            return middle
    return -1

# function to implement exponential search
def exponential_search(arr, key):
    # base case
    if arr[0] == key:
        return 0

    # starting with 1th index
    i = 1
    n = len(arr)
    # trying to search for first exponent j, for which 2^j is greater than key element
    # that is to find if the current element is smaller than key, and since it is sorted, then we need to increase the range by doubling it
    # also to avoid going out of bounds, we should ensure the invariant : i < n - 1
    while i < n - 1 and arr[i] <= key:

        i *= 2
        print(i)

    # lower bound will be i/2 , since we already have doubled then we have found greater number,
    # and higher bound will be whatever last greater number index we have found
    return binary_search(arr, i//2, i, key)

# driver function
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 20]
    key = 10
    index = exponential_search(arr, key)
    if index == -1:
        print("element not found !")
    else:
        print(f"element found at : {index}")
