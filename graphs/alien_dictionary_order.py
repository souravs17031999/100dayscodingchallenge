# Alien uses the some alien language using the same 'a-z' letters but the order of those chars can maybe or maybe not different than we use.
# Program for finding the order of letters, given Sorted dictionary of words in that alien language.
# Examples:
#
# Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
# Output: Order of characters is 'b', 'd', 'a', 'c'
# Note that words are sorted and in the given language "baa" 
# comes before "abcd", therefore 'b' is before 'a' in output.
# Similarly we can find other orders.
#
# Input:  words[] = {"caa", "aaa", "aab"}
# Output: Order of characters is 'c', 'a', 'b'
# ------------------------------------------------------------------------------------------------------------------------------------------
# We need to first understand that in the normal dictionary, how do we get the order of letters ?
# let's say :
# cat   ---   
#         | =>  we know cat comes before dog as 'c' comes before 'd' 
# dog   ---
# matching same chars in both strings will not be beneficial as we can't get any info from it, but if there are unmatching chars in the string, then it can be good, 
# we are able to find the order of chars/letters using the first unmatched char in both the strings.
# Similarly, we can do for this alien language, since we know it's sorted in the order, so if any unmatched char comes before unmatched char in the second string, 
# then, it means we have got some order.
# similarly, go for all the words and get the order of all the letters.
#
#
#               a -> c
#               -------
#              |      |
# baa | abcd | abca | cab | cad
# ^     ^  ^      ^     ^     ^
# |     |  |      |     |     |
# -------   -------      ------
#   |          |            
#  b  -> a   d -> a       b -> d
#
#
# So, there are 4 important info  : [b -> a, d -> a, a -> c, b -> d]
# Now, if we observe carefully, then this can be represented as a graph of directed edges of all unmatched chars pairs from all words.
# Then, we can perform "topological sorting", to perform the relative ordering of all chars.
# As, we can get the ordering of any pair of chars by using only DFS but we need to get relative ordering of all chars of pairs, hence, we need topological sorting.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(N * max_size_of_word) + 0(E + V), N is total words in the array, max_size_of_word is maximum size of all the possible words in the dict, E, V are edges and nodes 
# of graph.

from collections import deque, defaultdict as dd

def dfs(source, visited, graph, stack):
    
    visited.add(source)
    for i in graph[source]:
        if i not in visited:
            dfs(i, visited, graph, stack)
    
    stack.append(source)

def topological_sort(nodes, graph):
    
    visited = set()
    stack = deque()
    for i in nodes:
        if i not in visited:
            dfs(i, visited, graph, stack)
    
    while stack:
        print(stack.pop(), end = " -> ")
    

def get_order_dict(words):
    
    graph = dd(list)
    nodes = set()
    
    for i in range(len(words) - 1):
        ptr1 = 0
        ptr2 = 0
        n1 = len(words[i])
        n2 = len(words[i + 1])
        while ptr1 < n1 and ptr2 < n2 and words[i][ptr1] == words[i+1][ptr2]:
            ptr1 += 1
            ptr2 += 1
            
        nodes.add(words[i][ptr1])
        nodes.add(words[i+1][ptr2])
        graph[words[i][ptr1]].append(words[i+1][ptr2])
    
    topological_sort(nodes, graph)
    

words1 = ["baa", "abcd", "abca", "cab", "cad"]
words2 = ["caa", "aaa", "aab"]
get_order_dict(words1)   
print()
get_order_dict(words2)

# b -> d -> a -> c -> 
# c -> a -> b -> 
