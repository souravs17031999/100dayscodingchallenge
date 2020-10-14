# Program to generate all combinations using recursion + backtracking.

class Solution:
    
    def combinations(self, subset, index, n, k, output):
        if len(subset) == k:
            output.append(subset.copy())
            return 
    
        for i in range(index, n + 1):
            subset.append(i)
            self.combinations(subset, i + 1, n, k, output)
            subset.pop()

        
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        self.combinations([], 1, n, k, output)
        return output
