# Program for computing longest consecutive subsequence for the given string.
# Given, ex. string : [1, 9, 3, 10, 4, 20, 2], output : [1, 2, 3, 4] => "4"
# ----------------------------------------------------------------------------------
# Naive approach : So, we can observe first if we sort the array then we can get consecutive sequence in one go.
# Then, we can simply keep a count variable for counting till arr[i] + 1 = arr[i + 1]
# and reintializae count = 1 if it is not true, and keep updating max using this count.
# This would take 0(N*log(N)), with Space : 0(1).
# ----------------------------------------------------------------------------------
# Now, if we observe then we can find that for any consecutive subsequence we need to find the starting point
# of the given sequence as it should be consecutive.
# So, we can keep a extra hashtable, which can tell us if there is any arr[i] - 1 for every arr[i] which tells that the starting point is arr[i] - 1
# and so if it exists, then that is our starting point,
# and if it doesn't then it means current is the only starting point.
# we also keep checking for other consecutive elements in the hashtable when we found a starting point, and hence updating our max along with that.
# This would take 0(N) as we are only visiting all the elements once, and with space : 0(N).
# ----------------------------------------------------------------------------------

def compute_longest_subs(arr, n):

    s = set()
    for i in arr:
        s.add(i)
    ans = 0
    for i in range(n):

        if arr[i] - 1 not in s:

            j = arr[i]
            while j in s:
                j += 1

            ans = max(ans, j - arr[i])
    return ans

if __name__=='__main__':
    n = 7
    arr = [1, 9, 3, 10, 4, 20, 2]
    print("Length of the Longest contiguous subsequence is ")
    print(compute_longest_subs(arr, n))
