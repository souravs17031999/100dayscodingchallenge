# Program for optimal game strategy for making Player1 wins always.
# So, we need to compute the max. value of coins values possible from making Player 1 win in a two player game.
# There are two possible options allowed : either from first or last coin from a given row of coins.
# -----------------------------------------------------------------------------------------------------------------
# For a given value of subset from (i.....j),
# V(i, j) : max value we can definately win if it's our turn and only coins vi....vj remain
# ---------------------------------------------------------------------------------------------------------------
# Base cases :
# V(i, j) = Vi, i == j
# V(i, j) = max(vi, vj) j == i + 1
#
# [v1.....-vi- vi + 1........vj.....vn]
# V(i, j) = max{ min(v(i+1, j-1), v(i+2, j)) + vi), min(v(i, j-2), v(i+1, j-1) + vj) }
#                   ______________________            ______________________
#               pick vi                              pick vj
# --------------------------------------------------------------------------------------------------------------------
# first option is to choose if player1 choose first coin, and second option if we choose last coin.
# we need to choose the current value for the specific coin value + min(remaining which opponent player chooses as this  gives a guratee
# that atleast we will be having this much value as we don't have control over what player2 chooses in its turn.).
# ------------------------------------------------------------------------------------------------------------------
# TIME : 0(N^2), SPACE : 0(N^2)

# Python3 program to find out maximum
# value from a given sequence of coins

# Returns optimal value possible that
# a player can collect from an array
# of coins of size n. Note than n
# must be even
def optimalStrategyOfGame(arr, n):

	# Create a table to store
	# solutions of subproblems
	table = [[0 for i in range(n)]
				for i in range(n)]

	# Fill table using above recursive
	# formula. Note that the table is
	# filled in diagonal fashion
	# (similar to http://goo.gl / PQqoS),
	# from diagonal elements to
	# table[0][n-1] which is the result.
	for gap in range(n):
		for j in range(gap, n):
			i = j - gap

			# Here x is value of F(i + 2, j),
			# y is F(i + 1, j-1) and z is
			# F(i, j-2) in above recursive
			# formula
			x = 0
			if((i + 2) <= j):
				x = table[i + 2][j]
			y = 0
			if((i + 1) <= (j - 1)):
				y = table[i + 1][j - 1]
			z = 0
			if(i <= (j - 2)):
				z = table[i][j - 2]
			table[i][j] = max(arr[i] + min(x, y),
							arr[j] + min(y, z))
	return table[0][n - 1]

# Driver Code
arr1 = [ 8, 15, 3, 7 ]
n = len(arr1)
print(optimalStrategyOfGame(arr1, n))

arr2 = [ 2, 2, 2, 2 ]
n = len(arr2)
print(optimalStrategyOfGame(arr2, n))

arr3 = [ 20, 30, 2, 2, 2, 10]
n = len(arr3)
print(optimalStrategyOfGame(arr3, n))
