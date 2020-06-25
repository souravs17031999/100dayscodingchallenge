# Program for using inbuilt function for building stack
# deque is preferable for default use as it's compiler optimized

from collections import deque
from queue import LifoQueue

def stack1():
    stack = deque()
    stack.append(0)
    stack.append(1)
    stack.pop()

def stack2():
    stack = LifoQueue()
    stack.put(0)
    stack.put(1)
    stack.put(2)
    stack.get()

if __name__ == '__main__':
    stack1()
    stack2()
