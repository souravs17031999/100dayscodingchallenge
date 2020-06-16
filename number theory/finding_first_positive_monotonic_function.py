# Program to find the First positive number at which function gives positive value given function is monotonic
# Monotonicity means function is either increasing or decreasing.
# This means the data is in order -> sorted order.
# IDEA: Naive solution is to simply check at every number, the function's value but that will take 0(N) time.
# So, we can make use of binary search given the Monotonicity - order of data to decrease the time complexity to 0(lg(N)).


# defining a monotonic function
def f(x):
    return (x * x - 10 * x - 20)

# binary search function
# since we know that we have to pivot around "0" as we need to find the first positive value
def binary_search(low, high):

    while low <= high:
        mid = low + (high - low) / 2

        # if current mid value is positive and just before the value was negative or 0, then it means
        # we have found the first positive element
        if f(mid) > 0 and f(mid - 1) <= 0:
            return mid

        # otherwise if it is negative then, move to positive space
        elif f(mid) <= 0:
            low = mid + 1

        # else if it is already positive so we need to keep moving towards left (towards 0) as we need to find first positive value
        # so minimum will be better that's why we keep searching and narrowing down our search until we converge
        else:
            high = mid - 1

    return -1


# Here , we don't know what the search space is ! So, we are generating search space by doubling it (we can also go for more,
# but it is efficient (lg(n)) with base 2)

# function to return the first positive value
def find_first():

    # if it is the first index element
    if f(0) > 0:
        return 0

    # iterating and generating search space by setting low and high pointers using "i"
    # going till we get positive span
    i = 1
    while f(i) <= 0:
        i *= 2

    # going for binary search which will return if there is any existence of first positive element 
    return binary_search(i/2, i)


if __name__ == '__main__':
    print(find_first())
