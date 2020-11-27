# program to traverse the matrix diagonally in zig zag fashion
# logic is to find the heads of all the diagonals one by one and traverse them keeping in mind that all the even numbered indiced doagonal are reversed and others simply traverse from right to left in normal fashion.
# We know from observation that all the heads are starting from all elements from first row and all elements of last column
# Now, we also know for any element M(i, j) -> if going upwards then the element should be M([i-1], [j + 1]) and opposite M([i + 1], [j - 1]) when going downwards through a diagonal.
# so we need to keep a temp array to store the current elements of diagonals as a buffer and then keep transfering it to the original result array which is to be returned.
# Time complexity : 0(M * N) and space complexity : 0(K) where K is min(N, M)
#
# Input:
# [
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
# ---------------------------------------------------------------------------------------------------


def findDiagonalOrder(matrix):
        # intialize the result array
        result = []
        # check if matrix is empty then simply return the list otherwise apply our algorithm
        m = len(matrix)
        if m:
            n = len(matrix[0])
            # if the matrix contains only one element (one row, one column)
            if m == 1 and n == 1:
                result.append(matrix[0][0])
                return result
            # if matrix contains only one row
            if m == 1 and n != 1:
                result.extend(matrix[0])
                return result
            # if matrix contains only one column
            if n == 1 and m != 1:
                for i in matrix:
                    result.extend(i)
                return result
            # for all other general case, we need to move our pointer from all first row and then last column
            for i in range(m + n - 1):
                # temporary array for storing current buffer storage of diagonal elements
                temp = []
                # finding the ith, jth of head of current diagonal
                # row will be first row while traversing till the element of first row exhausts and keep traversing in last column
                r = 0 if i < n else i - n + 1
                # column will be same as our ith pointer which is changing , and then it will be fixed as the last column while traversing last column
                c = i if i < n else n - 1
                # move in the diagonal until one of the head pointers exhausts
                while(r <= m - 1 and c >= 0):
                    temp.append(matrix[r][c])
                    r += 1
                    c -= 1
                # if even ordered indiced diagonal, then reverse the temp array and move it to result array , ex. 0, 2, 4, 6..
                if i & 1:
                    result.extend(temp)
                # if odd numebred, then simply move it to result array  , ex. 1, 3, 5, 7, ....
                else:
                    result.extend(temp[::-1])
            return result
        else:
            return result

# There can be one another approach where we can try not to keep any buffer storage as temp array and simply keep traversing like the zig zag fashion in which we will be required to keep track of direction and then according to that head pointers.
# so, direction can be some boolean var which will be reversing in each iteration, then head pointers can be found by last tail diagonal traversal.
# like if we are coming downwards, then next head will be just below element if it's within the bounds , toherwise it will be in right
# similary , if we are moving upwards, then our next head will be right if within bounds, otherwise it will be just below (for outer bounds)
# in this case, space complexity will be 0(1) , although time complexity will remain same because traversal logic is same.
# main function


## IMPORTANT , THERE IS ANOTHER SIMPLEST SOLUTION WITH SAME TIME AND SPACE COMPLEXITY.
# IDEA: LOGIC IS THAT DIAGONALS ARE DEFINED BY THE SUM OF THE INDICES OF THE ELEMENTS.
# SO, ELEMENTES ON THE SAME DIAGONALS WILL HAVE SAME SUM AND IF WE CAN STORE THESE IN THE FORM OF DICTIONERY WHERE KEY IS SUM OF THE INDICES AND APPENDS ALL THE ELEMENT
# TO THE LIST AS VALUE OF THAT KEY.
# THEN, WE CAN CREATE OUR ANSWER LIST WHICH CAN SIMPLY REVERSE IF NEEDED (TEMP ARRAY REVERSAL BASED ON EVEN OR ODD DIAGONALS)
# TIME : 0(M*N), SPACE : 0(MIN(M, N))

def traverse(mat):

    # m denotes rows and n denotes columns
    m = len(mat)
    if m == 0:
        return []

    n = len(mat[0])
    if m == 1 and n == 1:
        return [mat[0][0]]


    # THIS DICTIONERY MAINTAINS KEY AS SUM OF THE INDICES WHICIH ARE ON THE SAME DIAGONALS
    # AND VALUE AS LIST OF ELEMENTS ON  THE SAME DIAGONALS
    diagonal_idx = {}

    for i in range(m):
        for j in range(n):
            if i + j not in diagonal_idx:
                diagonal_idx[i + j] = [mat[i][j]]
            else:
                diagonal_idx[i + j].append(mat[i][j])

    # CREATING OUR ANSWER LIST , IF DIAGONAL IS EVEN, REVERSE THE TEMP ARRAY STORED IN DICTIONERY , OTHERWISE SIMPLY APPEND IT TO OUR ORIGINAL ANSWER LIST
    ans = []
    for i, j in diagonal_idx.items():

        if i & 1:
            ans.extend(j)
        else:
            ans.extend(j[::-1])

    return ans


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(findDiagonalOrder(matrix))
