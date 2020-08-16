# Program for maximizing cut segments for fixed lengths -> p, q, r and given length of rod "L".
# EX. rod (L) : 11, p, q, r = 2, 3, 5.
# Now optimal length : 5
# --------------------------------------------------------------------------------------------------------------
# One key thing is to observe that not every segment is possible in the given rod, since segments are fixed.
# Now, this is an exhaustive search problem in which at every step, we are having three possible segments and so choices
# are possible, in which we want most optimal choice to maximize the cut segments.
# Here, For finding the maximum number of cuts that can be made in length ‘l’, find number of cuts made in shorter
# previous length ‘l-p’,’l-q’,’l-r’ lengths respectively.
# The required answer would be the max(l-p,l-q,l-r)+1 as one more cut should be needed after this to cut length 'l'.
# --------------------------------------------------------------------------------------------------------------
# Hence, we are going to use DP, TIME : 0(N).
# --------------------------------------------------------------------------------------------------------------
# NOTE : Not all segments are possible, so we have to keep a check on that.

def compute_max_cut_segment(l):

    dp = [-1] * (l + 1)
    dp[0] = 0 # base case

    for i in range(l + 1):

        if dp[i] == -1:
            continue

        # if segment p is possible
        if i + p <= l:
            dp[i + p] = max(dp[i + p], dp[i] + 1)

        if i + q <= l:
            dp[i + q] = max(dp[i + q], dp[i] + 1)

        if i + r <= l:
            dp[i + r] = max(dp[i + r], dp[i] + 1)

    return dp[l]        

if __name__ == '__main__':
    l = 11
    p, q, r = 2, 3, 5
    print(compute_max_cut_segment(l))
