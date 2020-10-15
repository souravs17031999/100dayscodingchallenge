# Program for checking if the robot after taking some moves defined by "U", "D", "L", "R" is able
# to come back to origin after starting from origin itself.
# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves,
# judge if this robot ends up at (0, 0) after it completes its moves.
#
# The move sequence is represented by a string, and the character moves[i] represents its ith move.
# Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all
# of its moves, return true. Otherwise, return false.
#
# Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once,
# "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
# -------------------------------------------------------------------------------------------------------------------------------
# Example 1:
#
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
# Example 2:
#
# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
# Example 3:
#
# Input: moves = "RRDD"
# Output: false
# Example 4:
#
# Input: moves = "LDRRLRUULR"
# Output: false
# --------------------------------------------------------------------------------------------------------------------------------
# We can visualize the directions as shown below :
#          (1, 0)
#           |
# (0, -1)-- (0, 0) -- (0, 1)
#           |
#         (-1, 0)
#
# so, we can start from origin, take current running sum, and if after taking all the moves, if we reach "0" in x, y positions,
# then return True else False.
# ---------------------------------------------------------------------------------------------------------------------------------
# TIME: 0(N), N IS LENGTH OF MOVES, SPACE : 0(1).

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir = {'U' : (1, 0), 'D' : (-1, 0), 'L' : (0, -1), 'R' : (0, 1)}

        curr_pos_x, curr_pos_y = 0, 0
        for i in moves:
            curr_pos_x += dir[i][0]
            curr_pos_y += dir[i][1]

        return curr_pos_x == curr_pos_y == 0
