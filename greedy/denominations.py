# Given denominations : [1, 2, 5, 10, 20, 50, 100, 500, 1000]
# We need to minimize the number of coins possible to make upto some value V.
# ------------------------------------------------------------------------------
# From our intuition, we can apply our greedy approach for firstly choosing
# coins of maximum denominations as much possible.
# But this algorithm only works for indian denominations for specific cases.
# For general denominations, we need to use DP.
# ------------------------------------------------------------------------------
# TIME : 0(N*log(N))
# ------------------------------------------------------------------------------

def compute_min_den(V):


    deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    ans = []
    for i in range(8, -1, -1):

        while V >= deno[i]:
            V -= deno[i]
            ans.append(deno[i])

    print(ans)

if __name__ == '__main__':
    n = 93
    print(compute_min_den(n))
