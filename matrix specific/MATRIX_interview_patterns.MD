# WHEN IN INTERVIEW, LOOK OUT FOR PATTERNS:
* Converting between matrix and array is useful :
```
2d[i][j] = 1d[i * n + j], n is cols , (i, j) is index in matrix.
```
* Converting between array and matrix :
```
index of array => idx, so row_idx, col_idx = idx / cols, idx % cols, mat[row_idx][col_idx]
```
* Look for staircase algorithm for sorted matrices.
* Elements indices on the same diagonals sum up to same values.
* Transposing is like swapping either in upper half or lower half.
* Transpose and rotation is related.
* Look for boundary algorithm (keeping four pointers for setting boundaries) for different types of traversals.
* Computing prefix sum matrix and suffix sum matrix can be really helpful.
## while computing prefix or suffix, we compute first by row and then col, or vice-versa.
## Do row wise addition prefix sum
## Then, do column wise addition prefix sum
# Computing subqueries for sum would be like :
```
Sum (i, j) -> (x, y) => P[x][y] + P[i - 1][j - 1] - P[i - 1][y] - P[x][j - 1]
```
