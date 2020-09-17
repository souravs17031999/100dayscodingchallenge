# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

# Approach will be to loop around for each char from every matrix, and check if the first char of pattern/word
# matches, then go for DFS starting from that char.
# DFS will go for all four directions (as all four are allowed here), horizontally as well as vertically.
# We will take care of out of bound cases, and other base cases like when pointer of pattern matches
# with length of pattern/word.
# Also to mark visited position, we need to place "#" or any other char "$" so that next recursion call stack
# will not be going to that cell again, hence to avoid infinite loop.
# After recursion call stack finishes for that DFS call, we again unmark and set its original value.

# -------------------------------------------------------------------------------------------------------
# TIME : 0(M * N * 4 ^ (S)), S IS LENGTH OF WORD, M IS LENGTH OF NROWS, N IS LENGTH OF WORDS.
# SPACE : 0(S)
# S IS LENGTH OF WORD AND EVEYRTIME WE HAVE FOUR CHOICES.

class Solution:
    def dfs(self, board, word, i, j, nrow, ncol, ptr):

        l = len(word)

        if l == ptr:
            return True

        if i < 0 or i >= nrow or j < 0 or j >= ncol:
            return False

        if board[i][j] == word[ptr]:
            temp = board[i][j]
            board[i][j] = "#"
            res = self.dfs(board, word, i, j + 1, nrow, ncol, ptr + 1) or self.dfs(board, word, i, j - 1, nrow, ncol, ptr + 1) or self.dfs(board, word, i + 1, j, nrow, ncol, ptr + 1) or self.dfs(board, word, i - 1, j, nrow, ncol, ptr + 1)

            board[i][j] = temp

            return res
        else:
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow, ncol = len(board), len(board[0])

        if len(word) > nrow * ncol:
            return False

        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, nrow, ncol, 0):
                        return True

        return False
