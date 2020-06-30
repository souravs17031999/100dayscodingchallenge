# Program for computing minimum of stack - in 0(1) time but it is now allowed to modify basic structure of stack
# TIME : 0(1)

from collections import deque

# STRUCTURE STACK
class Stack:

    # initialize the stack using pair type where [i, j] -> i : stack element, j : min_ele till front of stack
    def __init__(self):
        self.stack = deque(tuple())

    # function for pushing the element onto stack in 0(1)
    def push(self, x):

        if not self.stack:
            self.stack.append((x, x))
            return

        min_ele = min(x, self.stack[-1][0])
        self.stack.append((x, min_ele))

    # function for popping the element from stack in 0(1)
    def pop(self):

        if not self.stack:
            raise Exception ("POP INDEX ERROR !")

        pop_value = self.stack.pop()
        return pop_value[0]

    # function for getting minimum from stack in 0(1)
    def getMin(self):
        if not self.stack:
            raise Exception ("POP INDEX ERROR !")

        min_value = self.stack[-1][1]
        return min_value


# driver testing function
if __name__ == '__main__':
    arr = [41, 31, 68, 86, 80, 27, 61, 12, 12, 25]
    s = Stack()
    for i in arr:
        s.push(i)

    print(f"min_value : {s.getMin()}")
    print(s.pop())
    print(f"min_value : {s.getMin()}")
    print(s.pop())
    print(f"min_value : {s.getMin()}")
    print(s.pop())
    print(f"min_value : {s.getMin()}")
