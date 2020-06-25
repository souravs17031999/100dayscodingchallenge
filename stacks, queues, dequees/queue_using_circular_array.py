# program to implement queue using circular arrays

# class for constructing queue
class queue:
    def __init__(self, size):
        self.front = self.rear = -1
        self.arr = [None] * size
        self.size = size

    # function for pushing the element into front of queue
    def enqueue(self, x):
        # if queue is full
        if (self.rear == self.size - 1 and self.front == 0) or (self.rear == self.front - 1):
            print('Overflow detected !')
        # if first element is to be inserted
        elif (self.front == -1):
            self.rear = self.front = 0
            self.arr[self.rear] = x
        # for other elements
        else:
            self.rear = (self.rear + 1) % self.size
            self.arr[self.rear] = x

    def dequeue(self):
        # underflow check
        if self.front == self.rear == -1:
            print('underflow condition')
        # if single element is left to be deleted
        elif self.front == self.rear:
            self.front = self.rear = -1
        # for other elements , now here rear index will be more than highest index of array, so to be in the same range, we use modulus
        else:
            self.front = (self.front + 1) % self.size

    def print_queue(self):
        # empty queue check
        if self.front == self.rear == -1:
            print('Empty queue !')
            return
        # for normal front to rear TRAVERSAL
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(f"{self.arr[i]} ->", end = " ")
            print()
        # now if front is ahead of rear due to rear being more than highest index and taking approoriate value as per modulus surpassing the highest value in the indices of array
        else:
            for i in range(self.front, self.size - 1):
                print(f"{self.arr[i]} ->", end = " ")
            for i in range(0, self.rear + 1):
                print(f"{self.arr[i]} ->", end = " ")
            print()

# main function
if __name__ == '__main__':
    q = queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.print_queue()
    q.dequeue()
    q.dequeue()
    q.print_queue()
    q.enqueue(100)
    q.enqueue(200)
    q.print_queue()
    q.dequeue()
    q.print_queue()
