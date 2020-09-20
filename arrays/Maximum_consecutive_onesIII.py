# Program for computing longest length of consecutive ones
# with atmost k flips allowed to convert 0 to 1.

# Efficient solution using sliding window in O(N)

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start, max_z = 0, 0
        count = 0
        for end in range(len(A)):
            if A[end] == 0:
                count += 1
            
            while count > K:
                if A[start] == 0:
                    count -= 1
                start += 1
            
            max_z = max(max_z, end - start + 1)
        return max_z

