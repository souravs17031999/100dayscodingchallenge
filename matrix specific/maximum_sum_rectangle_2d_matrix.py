# Program for computing maximum sum for submatrices of all possible from a given rectangle 2 -D matrix.
# Naive would be to generate all the possible submatrices for the given matrix and compute the sum and update the max_sum in the following way
#
#  [ 1 2 3 4 ]
#  [ 4 5 6 7 ]
#  [8 9 10 11]
#  Now, we need to observe that for generating any submatrix (rectangle), we just need two points -> upper left and bottom right.
# But overall we need to traverse all the way from top left corner to bottom right corner in max 0(rows * cols) steps.
# and so we do this for both, thus total computations : 0(rows^2 * cols^2)
# Then, we get the sum in 0(rows * cols) inside the above four loops making it total six loops but total complexity remains same  : 0(N^4)
# Can we do better ?
# It is quite evident from the above logic that we are duplicating the work for summing the submatrices, hence overlapping subproblems,
# giving us the hint for DP.
# The way we do here , is that we keep four pointers for getting the four boundaries named as left, right, top, bottom
# Now, for every pair of top, bottom columned pair, we iterate and so we generate all submatrices starting from left and ending at right,
# now we keep a running sum in a extra temp array (this is the crux of the algo), now this running sum from one column starting from left
# to right column, will help us to avoid recomputing the sums again again for submatrices and to get top and bottom of max submatrix,
# we apply kadane's algo to the temp array which indicates which rows contains maximum sum elments.
# Combining all the information obtained above, we can keep updating the max_sum overall and along with that we can keep a pointer for the
# submatrices boundary having the max_sum.
# TIME : 0(N ^ 3), SPACE : 0(N), IN TERMS OF ROWS, COLS: TIME : 0(COLS ^ 2 * ROWS), SPACE : 0(ROWS)

#   LR                                         L   R
#  [ 1 2 3 4 ]       [0]     [1]              [ 1 2  3 4]       [3]
#  [-1 4 0 3 ]    => [0] =>  [-1]  =>         [-1 4  0  3]   => [3]
#  [-9 3 -1 -4]      [0]     [-9]             [-9 3  -1 -4]     [-6]      .......... SIMILARLY MORE....
#
# ---------------------------------------------------------------------------------------------------------

import sys
def max_sum_row_wise(temp, start, end, rows):
    curr_sum, max_sum = 0, -sys.maxsize-1
    s = 0
    for i in range(rows):
        curr_sum += temp[i]
        if curr_sum < temp[i]:
            curr_sum = temp[i]
            s = i

        if max_sum < curr_sum:
            max_sum = curr_sum
            start[0] = s
            end[0] = i

    return max_sum

def compute_max_sum_matrix(mat, ROWS, COLS):
    max_sum = -sys.maxsize-1
    final_left, final_right, final_top, final_bottom = None, None, None, None
    start, finish = [0], [0]
    for left in range(COLS):
        temp = [0] * ROWS
        for right in range(left, COLS):

            for i in range(ROWS):
                temp[i] += mat[i][right]

            curr_max = max_sum_row_wise(temp, start, finish, ROWS)

            if max_sum < curr_max:
                max_sum = curr_max
                final_left = left
                final_right = right
                final_top = start[0]
                final_bottom = finish[0]

    return max_sum, final_left, final_right, final_top, final_bottom

def pretty_print(mat, left, right, top, bottom):
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            print(mat[i][j], end = " ")
        print()

if __name__ == '__main__':
    M = [[1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]]
    max_sum, left, right, top, bottom = compute_max_sum_matrix(M, len(M), len(M[0]))
    print(f"MAX SUM : {max_sum}")
    pretty_print(M, left, right, top, bottom)
