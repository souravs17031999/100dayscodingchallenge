# Program to return a set of lucky numbers given m * n distinct numbers in the matrix.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
# Example 1:
#
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
# Example 2:
#
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:
#
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# ------------------------------------------------------------------------------------------------------------------------
# Brute force way for checking all lucky numbers will be like for we traverse through all rows and all columns, and get minimum for all rows and get maximum
# for all columns, so getting min will be in 0(N) and we do this for all rows, so, 0(M * N), similarly we go for all columns, 0(N * M), so whichever element satisfies above 
# property that will be lucky number, so overall it will be 0(M ^ 2 * N ^ 2).
# Can we do better than this ?
# As we can see we are repeating computations for min/max calculations, so we need to preprocess min and max for all rows and cols, then we can simply check if 
# any element is in both min and max array that will be the lucky number.
#
# mat :  [3, 7, 8]
#        [9, 11, 13] 
#        [15, 16, 17]
#
# min : [3, 9, 15]
# max : [15, 16, 17]
# As we can see "15" is in both array, so it is lucky number.
# TIME : 0(M * N), SPACE : 0(M + N)
# ------------------------------------------------------------------------------------------------------------------------
import sys 
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        rows, cols = len(matrix), len(matrix[0])
        
        minimum = [None] * rows
        maximum = [None] * cols
        
        for i in range(rows):
            minimum[i] = min(matrix[i])
        
        ptr = 0
        for j in range(cols):
            ptr = 0
            temp_max = -sys.maxsize-1
            while ptr < rows:
                temp_max = max(temp_max, matrix[ptr][j])
                ptr += 1
            
            maximum[j] = temp_max
        
        output = []
        
        maximum = set(maximum)
        for i in minimum:
            if i in maximum:
                output.append(i)
        
        return output
            
