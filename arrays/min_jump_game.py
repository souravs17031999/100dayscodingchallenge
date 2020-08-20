# Program for computing min number of jumps required to reach the end of array given positions of max jumps at each
# index of array.
# Now, we have already discussed about this in jump game reachable or not problem that naive solution will be recurision  +  backtrakcing
# which is going to be exponential.
# So, we will here try DP solution for minimizing the time complexity.
# Intutition is we can see the recursion tree for overlapping subproblems and alreayd optimal subtructure property exist :
# arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
#
#              [1, 9]
#                |
#               [3, 9]
#              /  |    \
#        [5, 9] [8, 9]  [9, 9]
#      / | | | \
#  [7,9][8,9][9,9][0,9][6,9]   ............
#   ................
#
# We can use bottom up approach DP.
# Intuition will be to have a extra 1-d array, which tells at every position minimum number of jumps reachable from 0 index to that index i.
# and we at every point ask , whether we take the minimum number of jump availale from last position or add new jump possible.
# TIME: 0(N^2).

import sys
def compute_min_jump(arr, n):

    if n == 0 or arr[0] == 0:
        return 0

    dp = [sys.maxsize] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if i <= j + arr[j] and dp[j] != sys.maxsize:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n - 1]

# ALTERNATE METHOD :
# ----------------------------------------------------------------------------
# TIME :  0(N), SPACE : 0(1)
# We use peak-valley approach, where we can think of this combination of peaks and valley where we keep checking for all the
# values, we move and jump and if at any point we are out of bound, then we can't reach the end.
# Otherwise, if we are in the range, we take that "jump" and reduce the "step" (which we can still take).
# ---------------------------------------------------------------------------
# python program to count Minimum number
# of jumps to reach end

# Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps(arr, n):
    # The number of jumps needed to reach the starting index is 0
    if (n <= 1):
    	return 0

    # Return -1 if not possible to jump
    if (arr[0] == 0):
    	return -1

    # initialization
    # stores all time the maximal reachable index in the array
    maxReach = arr[0]
    # stores the amount of steps we can still take
    step = arr[0]
    # stores the amount of jumps necessary to reach that maximal reachable position
    jump = 1

    # Start traversing array

    for i in range(1, n):
    	# Check if we have reached the end of the array
    	if (i == n-1):
    	    return jump

    	# updating maxReach
    	maxReach = max(maxReach, i + arr[i])

    	# we use a step to get to the current index
    	step -= 1;

    	# If no further steps left
    	if (step == 0):
    	# we must have used a jump
        	jump += 1

        	# Check if the current index / position or lesser index
        	# is the maximum reach point from the previous indexes
        	if(i >= maxReach):
        		return -1

        	# re-initialize the steps to the amount
        	# of steps to reach maxReach from position i.
        	step = maxReach - i;
    return -1


# Driver program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)

# Calling the minJumps function
print("Minimum number of jumps to reach end is % d " % minJumps(arr, size))


arr = [1, 3, 6, 1, 0, 9]
size = len(arr)
print('Minimum number of jumps to reach',
      'end is', compute_min_jump(arr, size))
