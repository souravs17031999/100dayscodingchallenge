# Program for getting minimum from queue in 0(1) time
# IDEA: logic is very similar to what we have done while implmenting getMin in stacks.
# We need to firstly maintain a queue (original) which is used for maintaining order of elements,
# Now, from observations, we can understand that we can't take just a extra queue and use it for enqueuing and dequeuing,
# so, now we understand that we need to also pop from back which is not possible in a basic queue and so we need doubly ended queue (deque)
# Hence, we will maintain a deque, which will help us in achiveing a order of increasing or decreasing depending on minimum or maximum respectively.
# Thus, while enqueuing, we will push the element normally to queue, and then in deque, we need to for first we will simply append the element,
# and then for other cases, while the back of deque is greater than the element being pushed, keep popping out from the deque.
# Then, append the new element into the deque
# Now, while popping , simple logic whenevr the front of both will match, we will pop out both, and whenevr it will not match, simply pop from queue.
# TIME : 0(1), SPACE : 0(N)

from collections import deque
import random

class Queue:

    def __init__(self):
        self.queue, self.deque = deque(), deque()

    def enqueue(self, x):

        self.queue.append(x)
        if not self.deque:
            self.deque.append(x)
        else:
            while self.deque and self.deque[-1] > x:
                self.deque.pop()
            self.deque.append(x)

    def dequeue(self):
        if not self.queue:
            raise Exception ("POP ERROR INDEX !")

        if self.queue[0] == self.deque[0]:
            self.queue.pop()
            self.deque.popleft()
        else:
            self.queue.pop()

    def getMin(self):
        if self.deque:
            return self.deque[0]
        else:
            raise Exception ("DEQUE EMPTY WARNING !")

    def pretty_print(self):
        print(f"Queue : {self.queue}")
        print(f"Deque : {self.deque}")

if __name__ == '__main__':
    l = [random.randint(0, 1000) for _ in range(10)]
    q = Queue()
    for i in l:
        q.enqueue(i)

    q.pretty_print()
    print(f"getMin : {q.getMin()}")
    q.dequeue()
    q.pretty_print()
    print(f"getMin : {q.getMin()}")
