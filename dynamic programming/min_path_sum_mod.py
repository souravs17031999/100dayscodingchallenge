# Program to compute min path sum with few deviations from already solved similar problem.
# Now, we are allowed to move to lower diagonally cells also in addition to just right and just down.
# --------------------------------------------------------------------------------------------------
# So, again at every point, there can be exhaustive set of possiblities we need to explore, and therefore
# this can be solved using recursion and backtracking.
# At every point we can submit to the following recurrence relations :
# dp(m, n) = cost(m, n) + min((m - 1, n), (m, n - 1), (m - 1, n - 1))
# dp[m][n] will store the minimum cost to reach cell(m, n) chosen from all set of possiblities.
# ------------------------------------------------------------------------------------------------------
# Since, again recursion can be exhaustive , therefore time is exponential.
# ----------------------------------------------------------------------------------------------------
# So, we apply DP and memoize.
# ---------------------------------------------------------------------------------------------------
# # def minCost(cost, m, n): 
#
#     # Instead of following line, we can use int tc[m+1][n+1] or
#     # dynamically allocate memoery to save space. The following
#     # line is used to keep te program simple and make it working
#     # on all compilers.
#     tc = [[0 for x in range(C)] for x in range(R)]
#
#     tc[0][0] = cost[0][0]
#
#     # Initialize first column of total cost(tc) array
#     for i in range(1, m+1):
#         tc[i][0] = tc[i-1][0] + cost[i][0]
#
#     # Initialize first row of tc array
#     for j in range(1, n+1):
#         tc[0][j] = tc[0][j-1] + cost[0][j]
#
#     # Construct rest of the tc array
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]
#
#     return tc[m][n]
