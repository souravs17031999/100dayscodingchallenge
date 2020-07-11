# Program to compute kth root of given number n.
# So, we have to find the greatest integer x, for which x^k <= n is true.
# # IDEA: naive approach is to simply go on linear searching from 1 to n, and stop whenever we find
# the above condition to be satified, this way we get biggest integer satifying above condition.
# But that can take n*log(k) for computing this integer and for range queries, this may take up to:
# t*n*log(k).
# Now if we observe carefully, we can see search space from 1 to n is monotonic (sorted ordering in ascending manner)
# We can apply binary search and this reduces time complexity to log(n)*log(k).

# this computes and checks power in log(k) time.
def isPow(n, k, x):
    return x ** k <= n

# function to apply binary search in log(N)
def compute_pow(n, k):
    start, end = 1, n
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if isPow(n, k, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return mid

# driver test function
if __name__ == '__main__':
    n, k = 1000000000000, 10
    print(compute_pow(n, k))
