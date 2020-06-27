# program to desing the special data structure for implementing push, pop, top, getMin functions in 0(1) time.
# Logic is to maintain two stack one for main operations push, pop and top , and the
# other for maintaining minimum element always at the top of it.
# using appropritate conditions while pushing and popping , we can maintain
# the top element as always keeping minimum in second stack.

# THERE ARE TWO VARIANTS FOR THIS -
# FIRST LOGIC : when pushing the element into the stack, we compare whichever of (top, element being pushed) is minimum, that gets pushed onto the both stack
# main stack as well as MinStack
# When popping, pop from both stacks

# Here TIME FOR getMin : 0(1), SPACE : 0(N)
# Now, this is little bit inefficient, for ex. [30, 20, 10, 50] is being pushed onto stack, so when we are pushing we will push anyhow duplicate irrelevant
# elements which is not required , like in the above example we pushed 'N' no. of elements (whichever is minmum) in MinStack :  [30, 20, 10, 10]
# but we can do better surely - but how and if we can reduce the space required for this probem (<N elements being pushed in MinStack on average) though
# in worst case it will be same (0(N)) ?

# Space optimized logic goes like this, when we try to push the element, then we only push the element ito the MinStack, only when the element being pushed
# is smaller than , the top of the MinStack , and in this way we will be pushing lesser elements onto the stack on average
# now, when popping, we only pop when the top of both stacks match, obviosuly because it is the min elment then being popped out, otherwise simply pop
# from the main stack

from collections import deque
import random

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack, self.min = deque(), deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min:
            if x <= self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self) -> None:

        if len(self.stack):
            if self.stack[-1] == self.min[-1]:
                self.stack.pop()
                self.min.pop()
            else:
                self.stack.pop()

        else:
            raise Exception ("POP INDEX ERROR !")

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min):
            return self.min[-1]

    def pretty_print(self):
        print(f"stack : {self.stack}")
        print(f"Minstack : {self.min}")

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
