# program to desing the special data structure for implementing push, pop, top, getMin functions in 0(1) time.
# ALREADY WE HAVE SEEN OTHER VERSIONS FOR 0(1) TIME, 0(N) SPACE.
# NOw, in this part, we will see 0(1) time and 0(1) space.
# IDEA: logic is to have just one stack for our stack creation for holding elements for push and pop operations and maintain one extra variable
# which will hold the value of minimum of stack from current state of stack.
# So, now the question is how do we update the values of this min_ele ?
# Mathematically proven statements, shows that 2*x - y is smaller than y.
# We can use this , while pushing elements, if our  element being pushed is smaller than current min_ele, then we need to insert (2*x - min_ele) onto stack
# and make the min_ele equal to element being pushed (also we have initialized min_ele to the first element being pushed).
# Also, now while popping the element, we again check if element being popped out is smaller than the min_ele,
# then we update the value of min_ele = 2*min_ele - element being popped out.
# and implement getMin which will always return the value of variable - min_ele
# TIME : 0(1), SPACE : 0(1)

from collections import deque
import random


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack, self.min_ele = deque(), None

    def push(self, x: int) -> None:

        if self.stack:
            if x <= self.min_ele:
                self.stack.append(2*x - self.min_ele)
                self.min_ele = x
            else:
                self.stack.append(x)
        else:
            self.stack.append(x)
            self.min_ele = x

    def pop(self) -> None:

        if len(self.stack):
            y = self.stack.pop()
            if y < self.min_ele:
                self.min_ele = 2*self.min_ele - y
                return y
            else:
                return y

        else:
            raise Exception ("POP INDEX ERROR !")

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_ele:
            return self.min_ele

    def pretty_print(self):
        print(f"stack : {self.stack}")

# driver function
if __name__ == '__main__':
    s = MinStack()
    l = [41, 31, 68, 86, 80, 27, 61, 12, 12, 25]
    for i in l:
        s.push(i)
    s.pretty_print()
    print(f"minimum : {s.getMin()}")
    s.pop()
    print(f"minimum : {s.getMin()}")
    s.pop()
    print(f"minimum : {s.getMin()}")
    s.pop()
    print(f"minimum : {s.getMin()}")
