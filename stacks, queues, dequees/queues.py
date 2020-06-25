# Program for constructing stack from scratch using linked list
# IDEA: logic is to add new node in the beginning of the linked list and delete it from the beginning of linked list
# All the operations are in TIME : 0(1), SPACE : 0(1)
# # IDEA: logic is to have two pointers front and rear which will help in achiveing efficiency.
# addition will be at the end of linked list, deletion from the beginning of linked list

# Node structure class
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

# Queue structure class
class Queue:

    # initialising front and rear pointers
    def __init__(self):

        self.front = None
        self.rear = None

    # function for enqueueing the queue (adding the element)
    def enqueue(self, x):

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
        self.rear = node

    # function for dequeueing the queue (deleting the queue)
    def dequeue(self):

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
        temp.next = None
        return pop_value

    # function to return bool value based on whether queue is empty or not
    def isEmpty(self):
        return self.front == None and self.rear == None

    # function for getting size of queue
    def getSize(self):
        count = 0
        ptr = self.front
        while ptr:
            count += 1
            ptr = ptr.next
        return count

# driver test function
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(f"Queue size : {queue.getSize()}")
    # print(queue.dequeue())
    # print(queue.dequeue())
    #
