Suppose you are given the following code:

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // constructor
  public void zero(printNumber) { ... }  // only output 0's
  public void even(printNumber) { ... }  // only output even numbers
  public void odd(printNumber) { ... }   // only output odd numbers
}
The same instance of ZeroEvenOdd will be passed to three different threads:

Thread A will call zero() which should only output 0's.
Thread B will call even() which should only ouput even numbers.
Thread C will call odd() which should only output odd numbers.
Each of the threads is given a printNumber method to output an integer. Modify the given program to output the series 010203040506... where the length of the series must be 2n.



Example 1:

Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously. One of them calls zero(), the other calls even(), and the last one calls odd(). "0102" is the correct output.
Example 2:

Input: n = 5
Output: "0102030405"

# -----------------------------------------------------------------------------------------------------

Use a for loop to print n times from zero thread, n//2 times from even, and (n+1)//2 times from odd to form 2*n-digit output.

Use two locks for the even / odd threads and a lock for the zero thread. Each time zero thread prints, it increments self.ct and determines whether to run even or odd thread next. Each time even or odd prints, it unlocks the zero thread.

# -----------------------------------------------------------------------------------------------------

import threading
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock_0 = threading.Lock()
        self.lock_1 = threading.Lock()
        self.lock_2 = threading.Lock()
        self.counter = 0

        self.lock_0.acquire()
        self.lock_1.acquire()

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.lock_2.acquire()
            printNumber(0)
            self.counter += 1
            if self.counter & 1:
                self.lock_1.release()
            else:
                self.lock_0.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n//2):
            self.lock_0.acquire()
            printNumber(self.counter)
            self.lock_2.release()


    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1)//2):
            self.lock_1.acquire()
            printNumber(self.counter)
            self.lock_2.release()
        
