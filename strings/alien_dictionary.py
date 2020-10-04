# Program to verify if the alien dictionary is given, then if the given list of words are sorted lexigraphically.
# The words are sorted lexicographically if and only if adjacent words are. This is because order is transitive: a <= b and b <= c implies a <= c.
# To check whether a <= b for two adjacent words a and b, we can find their first difference. 
# For example, "applying" and "apples" have a first difference of y vs e. After, we compare these characters to the index in order.
#
# Care must be taken to deal with the blank character effectively. If for example, we are comparing "app" to "apply", this is a first difference of (null) vs "l".
# Here is the implemnetation of above intution for algorithm : 
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# TIME: 0(N), N IS NUMBER OF WORDS IN THE WORD LIST.
# SPACE : 0(1)

class Solution:
    
    def compare(self, word1, word2, order_map):
        
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                if order_map[word1[i]] > order_map[word2[i]]:
                    return False
                break
        
        else:
            if len(word1) > len(word2):
                return False
        
        return True
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_map = {key:value for value, key in enumerate(order)}
        
        for i in range(1, len(words)):
            if not self.compare(words[i - 1], words[i], order_map):
                return False
        
        return True
