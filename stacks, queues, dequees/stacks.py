# Program for constructing stack from scratch using linked list
# IDEA: logic is to add new node in the beginning of the linked list and delete it from the beginning of linked list
# All the operations are in TIME : 0(1), SPACE : 0(1)

# Node structure class
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

# Stack structure class
class Stack:

    # initialising top of Stack
    def __init__(self):
        self.top = None

    # function for pushing the element onto stack
    def push(self, x):

        if not self.top:
            new_node = Node(x)
            self.top = new_node
            return

        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    # function for popping the element from stack
    def pop(self):

        if self.isEmpty():
            raise Exception ("Stack is already empty !")

        temp = self.top
        pop_value = temp.data
        self.top = self.top.next
        temp.next = None
        return pop_value

    # function for getting bool value in return of whether stack is empty or not
    def isEmpty(self):
        return self.top == None

    # function for getting size of stack
    def getSize(self):
        count = 0
        ptr = self.top
        while ptr:
            ptr = ptr.next
            count += 1
        return count

    def getTop(self):
        if not self.top:
            return None
        return self.top

# DRIVER TEST FUNCTION
if __name__ == '__main__':
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    print(f"stack size : {stack.getSize()}")
