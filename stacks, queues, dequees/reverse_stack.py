# Program to reverse the stack using one extra stack
# IDEA: logic is to use temporary stack and for each element time, one by one we can take out a top element from stack
# and then append other elements left to another temporary stack and then , push the element into original stack
# Now, we can again put back all other elements from temporary stack to original stack
# We can keep doing it until we have done it for all the elements once
# TIME : 0(N^2), N IS LENGTH OF STACK SIZE, SPACE : 0(N) 

from collections import deque

def reverse_stack(stack):
    n = len(stack)
    temp = deque()
    for i in range(0, n):

        top = stack.pop()

        for j in range(0, n - i - 1):
            temp.append(stack.pop())

        stack.append(top)

        for j in range(0, n - i - 1):
            stack.append(temp.pop())

if __name__ == '__main__':

    stack = deque()
    stack.append('a')
    stack.append('b')
    stack.append('c')
    stack.append('d')
    reverse_stack(stack)
    print(stack)
