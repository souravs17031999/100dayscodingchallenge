# program for generating substrings and subsequences for a given array/string.

# program for generating subarrays/ substrings
# TIME : 0(N^2).

def gen_subarray(arr, n):
    print('All generating subarrays/substrings : ')
    # iterate through the list by keeping one point at one side
    for i in range(n):
        # the other point at other side
        for j in range(i, n):
            # now slice through i to j
            print(arr[i:j+1])


# program for generating subsequences
# IDEA: this is based on the fact that we can generate 2**n - 1 subsequences like counting in binary terms 000..00 till 11...11 and this can be useful here like when we want to print the subsequence , 
# then we can simply test the following condition by anding the counter with all possible sequences of bit shifts by 0, 2, 4, 8.... so that all of them can be generated
# So, we go one by one for all binary strings like 0, 1, 2, 3, ... 2**n-1, and check for all bit possible (till length of given string), so that whichever bit is set, that index of 
# of array is considered, so like in "010", only 2nd index element will be considered in one subset, and in like "110", only first and second index element will be in one subset.
# TIME : 0((2 ^ N) * (len(s))) ~ 0(2^N)

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
       
# Alternate method for subsequence generation/subsets generation or power set generation using recursion and backtracking : 
# Output is a 2d nested list containing all distinct subsets but can be modified for other uses as well.

class Solution:
    def subset(self, arr, index, temp, res):
        
        if index == len(arr):
            res.append(temp)
        else:
            self.subset(arr, index + 1, temp, res)
            self.subset(arr, index + 1, temp + [arr[index]], res)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.subset(nums, 0, [], output)
        return output
        

# main function
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    maximum_subarray(arr, n)
