# program for implementing queue using fixed length arrays

# class for constructing queue
class queue:
    # initializing front and rear pointers to 0th index and constructing arrays of fixed length
    def __init__(self, length):
        self.front = 0
        self.rear = 0
        self.arr = [0] * length
        self.maxLength = length
    # for pushing the elements to the end of queue, 0(1)
    def enqueue(self, x):
        # if array is full
        if self.rear > self.maxLength - 1:
            print('Overflow detected !')
        else:
            # putting the element in correct position and incrementing rear
            self.arr[self.rear] = x
            self.rear += 1
            print(f"enqueued {x}")
    # for popping the elements from the front of queue , 0(n)
    def dequeue(self):
        # if array contains only one element
        if self.front == self.rear:
            self.front = self.rear = 0
            print('Underflow detected !')
        else:
            # shift every element by 1 decrementing index by one
            for i in range(1, self.rear):
                self.arr[i - 1] = self.arr[i]
            # putting rear to correct position
            self.rear = self.rear - 1

    # defining size of the queue
    def get_size(self):
        self.first = self.front
        counter = 0
        while(self.first < self.rear):
            counter += 1
            self.first += 1
        print(f"The current queue size is {counter}")

    # display the queue
    def print_queue(self):
        if self.front == self.rear == 0:
            print("empty queue !")
        else:
            for i in range(self.front, self.rear):
                print(f"{self.arr[i]} ->", end = " ")
    # getting the front of queue
    def top(self):
        print(self.arr[self.front])

# main function
if __name__ == '__main__':
    q = queue(8)
    for i in range(10, 81, 10):
        q.enqueue(i)
    q.dequeue()
    q.dequeue()
    q.enqueue(100)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(200)
    q.print_queue()
