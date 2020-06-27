# Program for implementing stacks using queues
# IDEA: Logic has two variants - one in which we can make push operation costly, and pop operation efficient,
# another in which vice versa is true.
# below implmentation is for former idea :
# we need to maintain two queues, let's say q1 and q2 , one of the queue will be used for efficienly popping out the elements
# in 0(1) and then another queue will be used for maintaining push operation making it 0(N).
#----------------------------
# FOR EACH PUSH :
# enqueue into q2
# pop all the elements from q1 to q2, then swap the names q1<->q2
# FOR EACH POP :
# pop from q1
#-----------------------------

from collections import deque

class Stack1:

    def __init__(self):

        self.d1 = deque()
        self.d2 = deque()

    def push(self, x):

        self.d2.append(x)
        while self.d1:
            self.d2.append(self.d1.popleft())
        self.d1, self.d2 = self.d2, self.d1

    def pop(self):
        if self.d1:
            return self.d1.popleft()
        else:
            raise Exception ("POP index error !")


# IDEA: So, now we will implement latter idea,
# to make pop costly in 0(N) and push efficient in 0(1).
# FOR EACH PUSH :
# enqueue to q1
# FOR EACH POP :
#----------------------
# DEQUEUE ONE BY ONE ALL EXCEPT LAST FROM Q1 -> Q2 (enqueue)
# STORE LAST VALUE OF Q1, and pop it out.
# SWAP q1, q2
#----------------------

class Stack2:

    def __init__(self):
        self.d1 = deque()
        self.d2 = deque()

    def push(self, x):

        self.d1.append(x)

    def pop(self):

        if not self.d1:
            raise Exception ("raise Exception error !")

        while len(self.d1) != 1:
            self.d2.append(self.d1.popleft())

        pop_value = self.d1[0]
        self.d1.pop()

        self.d1, self.d2 = self.d2, self.d1
        return pop_value


# driver function
if __name__ == '__main__':
    print("Testing for stack 1:")
    s1 = Stack1()
    s1.push(0)
    s1.push(1)
    s1.push(2)
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    # print(s.pop())  # raise exception

    print("Testing for stack 2:")
    s2 = stack2()
    s2.push(0)
    s2.push(1)
    s2.push(2)
    print(s2.pop())
    print(s2.pop())
    print(s2.pop())
    # print(s2.pop())  # raise exception
