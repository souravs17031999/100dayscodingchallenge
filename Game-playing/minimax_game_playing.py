# Program for minimax game simulating.
# Player1 is us playing first match, player2 plays next.
# Now, Player1 always tries to maximize the score, and player2 always tries to minimize the score.
# So, overall both players plays optimally and we need to compute the optimal score of the game.
# -----------------------------------------------------------------------------------------------------
# Now, we can visualize the game using game tree.
# Backtracking algorithm, is used here so that exhaustive search is narrowed down quickly and we don't have to search for all paths.
# -----------------------------------------------------------------------------------------------------
# Every player has two possibilities to choose, and so it will either try to Maximize or Minimize depending on which player's turn it is.
# ------------------------------------------------------------------------------------------------------
# If we have scores (values on the leaf nodes) then, we can visualize the algorithm in the form of tree considering tree
# values of roots are stored in the array :
# leaf values : [3, 5, 2, 9, 12, 5, 23, 23]
# ------------------------------------------------------------------------------------------------------
#
#                       12
#                     /   \
#     I (MAX)       3      12
#                 / \     / \
#    II (MIN)   3    23  12  23
#             / \   /   \    .............
#    I (MAX) 3  2  5     23
#          / \ / \  /\    /\
# II(MIN) 3  5 2  9 12 5 23 23
# As we can see, root node gives the optimal score : 12
# --------------------------------------------------------------------------------------------------------

import math

def minimax (curDepth, nodeIndex,
			maxTurn, scores,
			targetDepth):

	# base case : targetDepth reached
	if (curDepth == targetDepth):
		return scores[nodeIndex]

	if (maxTurn):
		return max(minimax(curDepth + 1, nodeIndex * 2,
					False, scores, targetDepth),
				minimax(curDepth + 1, nodeIndex * 2 + 1,
					False, scores, targetDepth))

	else:
		return min(minimax(curDepth + 1, nodeIndex * 2,
					True, scores, targetDepth),
				minimax(curDepth + 1, nodeIndex * 2 + 1,
					True, scores, targetDepth))

# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))
