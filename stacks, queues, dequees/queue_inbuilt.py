# Program for using inbuilt function for building queue
# deque is preferable for default use as it's compiler optimized

from collections import deque
from queue import Queue as Q
from multiprocessing import Queue as MPQ

def queue1():
    q = deque()
    q.append(0)
    q.append(1)
    q.append(2)
    q.pop()

def queue2():
    q = Q()
    q.put(0)
    q.put(1)
    q.put(2)
    q.get()

def queue3():
    q = MPQ()
    q.put(0)
    q.put(1)
    q.put(2)
    q.get()

if __name__ == '__main__':
    queue1()
    queue2()
    queue3()
