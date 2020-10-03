# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
# ------------------------------------------------------------------------------------------------------------------------------------------------
# This problem can be formulated as a graph if we can represent all the word list along with start and end word as graph.
# Now, we need to actually find the shortest length of transformation so, BFS in the graph traversal will surely give us the shortest length of chain of transformations.
#
# TIME : 0((M ^ 2) * N), where M is the length of each word and N is the total number of words in the input word list.
# SPACE : 0((M ^ 2) * N)
# ------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        visited = set()
        is_present = False # flag for checking if endword is in the wordlist dict or not 
        for word in wordList:
            if word == endWord:
                is_present = True
            visited.add(word)

        if not is_present:
            return 0

        queue = deque()
        queue.append(beginWord)
        depth = 0
        # going for until queue is empty 
        while queue:

            depth += 1
            Q_size = len(queue)
            # for all the words at the same level (matched possible words)
            for _ in range(Q_size):
                curr = queue.popleft()
                # going for all the chars in each word 
                for i in range(len(curr)):
                    temp = list(curr)
                    # checking for all transforming , each character at a time replaced by digits from a-z (26 times, constant loop)
                    for c in range(97, 123):
                        temp[i] = chr(c)

                        if "".join(temp) == curr:
                            continue
                        if "".join(temp) == endWord:
                            return depth + 1

                        if "".join(temp) in visited:
                            queue.append("".join(temp))
                            visited.remove("".join(temp))
        
        return 0
