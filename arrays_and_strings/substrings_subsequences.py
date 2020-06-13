# program for generating substrings and subsequences for a given array

# program for generating subarrays/ substrings
def gen_subarray(arr, n):
    print('All generating subarrays/substrings : ')
    # iterate through the list by keeping one point at one side
    for i in range(n):
        # the other point at other side
        for j in range(i, n):
            # now slice through i to j
            print(arr[i:j+1])


# program for generating subsequences
# IDEA: this is based on the fact that we can generate 2**n - 1 subsequences like counting in binary terms 000..00 till 11...11 and this can be useful here like when we want to print the subsequence , then we can simply test the following condition by anding the counter with all possible sequences of bit shifts by 0, 2, 4, 8.... so that all of them can be generated
def gen_subseq(arr, n):
    print('All generating subsequence : ')
    # iterate for all possible consequences
    for counter in range(1, 2**n):
        # for all possible bits
        for j in range(0, n):
            # check the jth bit is set or not
            if counter & (1<<j):
                print(arr[j], end = " ")
        print()

# main function
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    maximum_subarray(arr, n)
