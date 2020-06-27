# Program to implement queue using stacks
# IDEA: logic has two variants -
# One of which makes enqueue costly, and other one makes deque costly
# former idea :
#------------------------
# FOR EACH ENQUEUEU :
# EMPTY THE stack1 TO stack2, AND THEN PUSH ELEMENT INTO stack1,
# PUSH BACK FROM stack2 -> stack1
# FOR EACH DEQUEE :
# POP FROM THE STACK1
#------------------------

from collections import deque

class Queue1:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def enqueue(self, x):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):

        if not self.stack1:
            raise Exception ("POP INDEX ERROR !")

        return self.stack1.pop()


# Now, implementing latter idea for making enqueue efficient, and making dequeue costly but it's also better than atleast previous
# approach and this approach for enqueue will be done in 0(1) and dequeue in amortized 0(1)
# IDEA: logic is to have two stacks and then,
# FOR EACH ENQUEUE :
# JUST PUSH TO STACK 1

# FOR EACH DEQUEUE:
# ---------------
# IF BOTH STACKS EMPTY, THEN ERROR !
# IF STACK2 EMPTY,
# THEN PUSH ALL ELEMENTS OF STACK1 -> STACK2
# NOW POP OFF FROM THE STACK2+++++++
#-----------------

class Queue2:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            raise Exception ("POP INDEX ERROR !")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

if __name__ == '__main__':
    q1 = Queue1()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    print(q1.dequeue())
    print(q1.dequeue())
    print(q1.dequeue())
    # print(q.dequeue())  # raise exception

    q2 = Queue2()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    # print(q2.dequeue())  # raise exception
