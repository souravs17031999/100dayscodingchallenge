# Program to check if a rat standing at source position (0, 0) in a  N * N 2-d grid can reach destination at [n - 1][n - 1].
# Note : only two moves are allowed => right and down.
# The problem can be varied based on how many moves are allowed at every position.
# EX.
# {1, 0, 0, 0}
# {1, 1, 0, 1}
# {0, 1, 0, 0}
# {1, 1, 1, 1}
# ---------------------------------------------------------------------------------------------------------
# We are going to use backtracking algorithm as we can see at every point we have two possible choices.
# So, at worst we can generate all the possible configurations and then check if we reached the destination or we can improve it
# by rejecting those paths which donont take us to solution using backtracking.
# since, we have always two positions :
# by observation we can say we can store the two possible cells (moves) we can make at every point,
# x_moves = [0, 1]
# y_moves = [1, 0]

def is_safe(maze, solution, n, curr_x, curr_y):

    if curr_x >= 0 and curr_x < n and curr_y >= 0 and curr_y < n and maze[curr_x][curr_y] == 1 and solution[curr_x][curr_y] == 0:
        return True
    return False

def solve(maze, solution, n, curr_x, curr_y, x_moves, y_moves, pos):

    if curr_x == n - 1 and curr_y == n - 1:
        print(solution)
        return True

    for i in range(2):
        new_x = curr_x + x_moves[i]
        new_y = curr_y + y_moves[i]

        if is_safe(maze, solution, n, new_x, new_y):
            solution[new_x][new_y] = pos
            if solve(maze, solution, n, new_x, new_y, x_moves, y_moves, pos + 1):
                return True
            solution[new_x][new_y] = 0

    return False

if __name__ == '__main__':

    maze = [[1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1]]

    x_moves = [0, 1]
    y_moves = [1, 0]
    n = len(maze)
    print(n)

    # we also want to print the path , so let's take another 2 -d array
    solution = [[0] * n for _ in range(n)]
    solution[0][0] = 1
    print(solution)
    print(solve(maze, solution, n, 0, 0, x_moves, y_moves, 1))
