# program to desing the special data structure for implementing push, pop, top, getMin functions in 0(1) time.
# Logic is to maintain two stack one for main operations push, pop and top , and the
# other for maintaining minimum element always at the top of it.
# using appropritate conditions while pushing and popping , we can maintain
# the top element as always keeping minimum in second stack.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if len(self.stack2):
            self.stack2.append(min(self.stack2[-1], x))
        else:
            self.stack2.append(x)

    def pop(self) -> None:
        if len(self.stack1):
            self.stack1.pop()
            self.stack2.pop()

    def top(self) -> int:
        if len(self.stack1):
            return self.stack1[-1]

    def getMin(self) -> int:
        if len(self.stack2):
            return self.stack2[-1]
