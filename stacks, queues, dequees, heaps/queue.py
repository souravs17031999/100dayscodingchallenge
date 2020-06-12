class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, x):
        if(self.empty()):
            new_node = Node(x)
            self.front = new_node
            self.rear = new_node
            return
        new_node = Node(x)
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if(self.empty()):
            return -1
        self.front = self.front.next
        if(self.front == None):
            self.rear == None

    def empty(self):
        if self.front == None:
            return True
        else:
            return False

    def print_queue(self):
        if(self.empty()):
            print('empty queue !')
            return
        ptr = self.front
        while(ptr != None):
            print(ptr.data, end = "->")
            ptr = ptr.next        

if __name__ == '__main__':
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.enqueue(4)
    q.enqueue(5)
    q.print_queue()
