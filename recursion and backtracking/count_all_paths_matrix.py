# recursive implementation for counting all the paths possible in a matrix
# given some starting point (assuming to be (0, 0) - leftmost corner and end point is at
# rightmost end corner)

def CountPath(rows, cols):
    if rows == 1 or cols == 1:
        return 1

    return CountPath(rows - 1, cols) + CountPath(rows, cols - 1)


print(CountPath(10, 10))
