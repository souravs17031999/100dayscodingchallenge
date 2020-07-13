# Program for sorting the strings lexographically and also we want that if lexographically similar string exist,
# then longer strings should come first before shorter one.
# We may have used simply sort which will sort the strings lexographically, but then we also want to maintain the invariant that longer
# string should come before shorter string if they are lexographically smaller.
# So, we need to make our custom sort function.
# So, we simply apply two for loops (on logic of bubble sort), then while traversing, we can check the above invariant.


# to check if swap is necessary and required, by maintaining the invariat that longer string should come before shorter one if they
# are lexographically similar.
def IsSwap(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] > s2[i]:
            return 1
        elif s1[i] < s2[i]:
            return -1
        i += 1

    if len(s1) < len(s2):
        return 1
    else:
        return -1

# simple two for loops for comparison passes similar to bubble sort
def sort_string(arr, n):

    for i in range(n):
        for j in range(n - i - 1):
            if IsSwap(arr[j], arr[j + 1]) > 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = ['bat', 'apple', 'batman']
    n = 3
    sort_string(arr, n)
    print(arr)
