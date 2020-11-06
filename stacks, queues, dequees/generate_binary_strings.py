# Program for generating binary strings of given value of "n".
# ---------------------------------------------------------------------------------------------------------------------------
# Examples:
#
# Input: n = 2
# Output: 1, 10
#
# Input: n = 5
# Output: 1, 10, 11, 100, 101
# ---------------------------------------------------------------------------------------------------------------------------
# Now, we can check for this using simply bin() function in python but we should not use any in-built function here.
# So, we are going to use queue here.
# ---------------------------------------------------------------------------------------------------------------------------
from collections import deque
def generate_binary(n):

    queue = deque()
    queue.append("1")

    while n > 0:

        n -= 1
        curr = queue.popleft()
        print(curr, end = " ")
        queue.append(curr + "0")
        queue.append(curr + "1")

generate_binary(5)
