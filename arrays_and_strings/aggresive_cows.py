# Program to determine the largest possible minimum distance between the C Cows placed at N bars.
# The cows are aggressive due to placing them nearby and so we are required to place them as afar
# as possible so that they do not hurt each other . Also given that each bar can only have one cow
# at a time.
# IDEA: Naive solution is to check for all possible combinations if the placemet of cows is possible or not in N(c)C.
# and that would take up a lot of time.
# If we observe the search space that we can identify is that minimum separation for the cows would be "0" and the maximum
# separation would be "n - 1".
# So, we can identify monotonic search spaces where we can apply binary search to reduce our search space.
# Now, if we think about it, we need to find basically in this search space, for every number is it possible to place the cows atleast
# at that distance apart ? if yes, then we can ignore left half space as it is already coveered, then we can move onto right half space.
# In this way, we can simply keep reducing search spaces and converge to the maximum possible distance between cows.
# TIME : 0(n*lg(n))

# function to check if min_sep is possible to keep cows at a safe distance
def isPossible(arr, n, cows, min_sep):
    last_cow = arr[0] # assign the first stall to the first cow
    count = 1
    # after that, we keep on checking if next coordinate (of stall/bar) is within the min_sep of current stall
    # and if yes, then increase the count (meaning we have allocated that stall to next cow )
    for i in range(1, n):
        if arr[i] - last_cow >= min_sep:
            last_cow = arr[i]
            count += 1
            if count == cows:
                return True

    return False


# function to compute maximum separation possible between each cow
def compute_distance(arr, n, cows):
    # firstly we need to sort the stalls position, so that we are following some kind of greedy
    # approach and to apply bin search.
    arr.sort()
    # defnining the search space
    start, end = 0, arr[n - 1] - arr[0]
    ans = 0
    # searching using bin search
    while start <= end:
        mid = (start + end) // 2
        if isPossible(arr, n, cows, mid):
            # if it's possible with this min_sep, then we go for more value to get max as much as possible
            ans = mid
            start = mid + 1
        else:
            # otherwise, we reduce our space by ignoring right half and searching left half space.
            end = mid - 1

    return ans

# driver test function
if __name__ == '__main__':
    arr = [1, 2, 4, 8, 9]
    n, cows = 5, 3
    print(compute_distance(arr, n, cows))
