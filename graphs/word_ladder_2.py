# Program to compute all the paths starting from beginWord to endWord and all these should be the shortest path from source to target.
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# * Only one letter can be changed at a time
# * Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# * Return an empty list if there is no such transformation sequence.
# * All words have the same length.
# * All words contain only lowercase alphabetic characters.
# * You may assume no duplicates in the word list.
# * You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
#  ["hit","hot","dot","dog","cog"],
#  ["hit","hot","lot","log","cog"]
# ]
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import defaultdict as dd, deque 

class Solution:
    
    def DFS(self, beginWord, endWord, graph, path, ans):
        
        path.append(beginWord)
        if beginWord == endWord:
            ans.extend(path)
            path.pop()
            return 
        
        for i in graph[beginWord]:
            self.DFS(i, endWord, graph, path, ans)
        
        path.pop()
        
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = dd(list)
        map = set()
        for i in wordList:
            map.add(i)
        
        queue = deque()
        queue.append(beginWord)
        visited = {}
        visited[beginWord] = 0
        
        while queue:
            curr = queue.popleft()
            temp = list(curr)
            for i in range(len(curr)):
                for c in range(97, 123):
                    temp[i] = chr(c)
                    if "".join(temp) == curr:
                            continue
                            
                    if "".join(temp) in map:
                        if "".join(temp) not in visited:
                            visited["".join(temp)] = visited[curr] + 1
                            queue.append("".join(temp))
                            graph[curr].append("".join(temp))
                        
                        elif visited["".join(temp)] == visited[curr] + 1:
                            graph[curr].append("".join(temp))
                
                temp[i] = curr[i]
        
        path = []
        ans = []
        self.DFS(beginWord, endWord, graph, path, ans)
        res = []
        temp = []
        for i in ans:
            temp.append(i)
            if i == endWord:
                res.append(temp)
                temp = []
        
        return res
                    
