# Problem is compute minimum time duration for painting the size of painting board divided into continuos segments.
# At a time, only one painter can paint the board.
# We have been K number of painters and the array containing size of the pieces (segments) which painters need to paint in minimum
# duration time.
# [ALso, if it is assumed that one board takes 1 unit of time to paint, then we simply have to apply the algorithm idea discussed below.
# But if some time is also given, then finally at the end, we need to multiply our answer with this time.]
# IDEA: Logic is to actually observe that we can define the search space to be our possible answer is in the range of 1....N.
# And we can apply binary search in this search space as it is monotonic in nature 1, 2, ....N.
# Now, we can check if the "mid" is feasible or not, if it is feasible, then we can go for more lesser value (going for left half space)
# as we need minimum. Otherwise, we can search for right half space.

# function to check if it is possible that given "max_len" can be whether painted by given "k" painters.
def isPossible(arr, n, k, max_len):
    total = 0
    num_painters = 1
    for i in range(n):
        if arr[i] > max_len:
            return False

        if total + arr[i] <= max_len:
            total += arr[i]
        else:
            total = arr[i]
            num_painters += 1
            if num_painters > k:
                return False
    return True

# function to compute minimum duration
def compute_time(arr, n, k, t):
    # maximum can be when we allocate one painter all the section of board.
    # minimum can be max of array as at a time, as in this allocation we can allot max to one painter
    start, end = max(arr), sum(arr)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if isPossible(arr, n, k, mid):
            # we update our answer
            ans = min(mid, ans)
            end = mid - 1
        else:
            start = mid + 1

    return (ans % 10000003) * t

# driver function 
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k, n, t = 3, len(arr), 5
    print(compute_time(arr, n, k, t))
