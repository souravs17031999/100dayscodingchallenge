# Given a dictionary of words and a method isstr() which returns whether a word is in dict or not, we need to
# find all possible words that can be formed from the given 2-d matrix where each cell represents a char.
# NOTE: We are allowed to move in all the 8 positions possible or valid from every point and no other char other than this can be used.
# EX.
# Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
#        boggle[][]   = {{'G*', 'I*', 'Z*'},
#                        {'U*', 'E*', 'K*'},
#                        {'Q*', 'S*', 'E*'}};
#       isWord(str): returns true if str is present in dictionary
#                    else false.
#
# Output:  Following words of dictionary are present
#          GEEKS
#          QUIZ
#
#
# TIME : 0((M * N * 8^(M*N)), SPACE : 0(M * N)
# --------------------------------------------------------------------------------------------------------------------------
# We are going to use backtracking to solve this problem.
# We know that at every point we have 8 possible cell moves choices, so we preprocess them already :
# row : [0, 0, 1, 1, -1, 1, -1, -1]
# col : [1, -1, -1, 1, 1, 0, 0, -1]


def is_safe(boogle, curr_x, curr_y, visited):
    if curr_x >= 0 and curr_x < len(boogle) and curr_y >= 0 and curr_y < len(boogle) and not visited[curr_x][curr_y]:
        return True
    return False

def solve(boggle, dictionary, visited, curr_x, curr_y, x_moves, y_moves, word):

    print(word)
    if word in dictionary:
        print(word)

    if len(word) == len(boogle):
        return

    for i in range(8):

        new_x = curr_x + x_moves[i]
        new_y = curr_y + y_moves[i]
        if is_safe(boogle, new_x, new_y, visited):
            visited[new_x][new_y] = True
            solve(boogle, dictionary, visited, new_x, new_y, x_moves, y_moves, word + boogle[new_x][new_y])
            visited[new_x][new_y] = False


# ALTERNATE BETTER METHOD :
# We should not go for all 8 comparisons here since it is not always possible to find the required char at either of the 8th positions
# rather we will use a hashmap and preprocess it and store all the occurences of the characters in a linked list along with the visited array.
# Now, whwenevr we move to new character, we simply check with hashmap wherever our char exists or if not exists at all (in all adjacent cells).

# More optimizations ?
# Using DFS + Trie
# We will use Following structure for contructing Trie :
#
# class TrieNode:
#
#     def __init__(self, data):
#         self.data = data
#         self.children = [0] * 256 # can also use 26 , ord(ch) - ord('a')
#         self.terminal = False
#         self.word = None  # this will be overall string build till current node

# We need to simply make two loops and traverse starting from every char (cell) in the 2-d matrix, and then call DFS from there.
# The dfs logic will be integrated with the Trie search logic and empty list can be taken and when the word is found in the Trie, we can simply push the word in the answer list.
# Finally, print the answer list.
# Searching for Trie : one by one we have search for the matching char by calling in all 8 directions and search like normally we do in Trie.

if __name__ == '__main__':

    boogle = [['G', 'I', 'Z'], ['U', 'E', 'K'], ['Q', 'S', 'E']]

    dictionary = ['GEEKS', 'FOR', 'QUIZ', 'GO']
    visited = [[False] * len(boogle) for _ in range(len(boogle))]
    x_moves = [0, 0, 1, 1, -1, 1, -1, -1]
    y_moves = [1, -1, -1, 1, 1, 0, 0, -1]
    word = ""
    # we have to apply backtrakcing/DFS from every char as we need to check for all possible
    # words that can be formed
    for i in range(len(boogle)):
        for j in range(len(boogle)):
            visited[i][j] = True
            solve(boogle, dictionary, visited, i, j, x_moves, y_moves, word + boogle[i][j])
            visited[i][j] = False
