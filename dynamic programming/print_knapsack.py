# Program to print those items which are included in the knapsack in the knapsack problem.
# Below knapsack is function which gives the dp table formed after applying the algorithm.
# We simply backtrack using the last index (the answer cell) till top left to form the answer in the way using two pointers row, col denoted by i, j.
# -------------------------------------------------------------------------------------------------------------------------------------------------------

def print_knapsack(W, wt, val, n):
    
    dp = knapsack(W, wt, val, n)
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print(dp[i][j], end = " ")
        print()
            
    i, j = n, W
    res = []
    while i > 0 and j > 0: 
            
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            res.append(i)
            j -= dp[i][j] - dp[i - 1][j]
            i -= 1
            
    
    print(f"items selected : {res[::-1]}")
   
