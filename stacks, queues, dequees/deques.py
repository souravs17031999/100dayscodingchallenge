# Program for constructing Deque from scratch using Doubly linked list
# It should support operations for adding and popping from both the ends in 0(1) time.

# structure node class
class Node:

    def __init__(self, x):

        self.data = x
        self.next = None
        self.prev = None

# structure deque class
class Deque:

    def __init__(self):
        self.front = None
        self.rear = None

    # function for adding the element from end of list
    def append(self, x):

        # if queue already empty, then create first new node,
        # and point both pointers to it
        if not self.front and not self.rear:
            node = Node(x)
            self.front = self.rear  = node
            self.rear = node
            return

        # in all other cases, rear will always to last added node
        node = Node(x)
        self.rear.next = node
        node.prev = self.rear
        self.rear = node

    # function for popping the elment from end of list
    def pop(self):
        # if queue is already empty
        if not self.front and not self.rear:
            raise Exception ("Queue already empty !")

        # if last element is to be deleted,
        # then making sure to delete all the references
        if self.front == self.rear:
            temp = self.rear
            self.front = self.rear = None
            pop_value = temp.data
            temp.next = None
            return pop_value

        temp = self.rear
        pop_value = temp.data
        self.rear = self.rear.prev
        self.rear.next = None
        temp.prev = None
        return pop_value

    # function for adding the element from beginning of list
    def appendleft(self, x):

        # if queue already empty, then create first new node,
        # and point both pointers to it
        if not self.front and not self.rear:
            node = Node(x)
            self.front = self.rear = node
            self.rear = node
            return

        # for other cases
        node = Node(x)
        node.next = self.front
        self.front.prev = node
        self.front = node

    # function for popping the elment from beginning of list
    def popleft(self):

        # if queue is already empty
        if not self.front and not self.rear:
            raise Exception ("Queue already empty !")

        # if last element is to be deleted,
        # then making sure to delete all the references
        if self.front == self.rear:
            temp = self.front
            self.front = self.rear = None
            pop_value = temp.data
            temp.next = None
            return pop_value

        # in all other cases, front will simply keep moving on
        # thereby deleting all the references which are being popped out
        temp = self.front
        pop_value = temp.data
        self.front = self.front.next
        self.front.prev = None
        temp.next = None
        return pop_value

    # function for getting size of deque
    def getSize(self):
        if self.front:
            count = 1
        else:
            count = 0

        ptr = self.front
        while ptr != self.rear:
            count += 1
            ptr = ptr.next

        return count

    def getFront(self):
        return self.front

    def getRear(self):
        return self.rear

    def isEmpty(self):
        return self.front == self.rear == None
                

# driver test function
if __name__ == '__main__':

    deque = Deque()
    deque.append(0)
    deque.append(1)
    deque.append(2)
    deque.appendleft(100)
    deque.appendleft(1000)
    print(deque.pop())
    print(deque.popleft())
    print(deque.popleft())
    print(deque.popleft())

    print(f"deque size : {deque.getSize()}")
