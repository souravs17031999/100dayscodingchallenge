Write a program that outputs the string representation of numbers from 1 to n, however:

If the number is divisible by 3, output "fizz".
If the number is divisible by 5, output "buzz".
If the number is divisible by both 3 and 5, output "fizzbuzz".
For example, for n = 15, we output: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.

Implement a multithreaded version of FizzBuzz with four threads. The same instance of FizzBuzz will be passed to four different threads:

Thread A will call fizz() to check for divisibility of 3 and outputs fizz.
Thread B will call buzz() to check for divisibility of 5 and outputs buzz.
Thread C will call fizzbuzz() to check for divisibility of 3 and 5 and outputs fizzbuzz.
Thread D will call number() which should only output the numbers.


# ----------------------------------------------------------------------------------------------------
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fsem = threading.Lock()
        self.bsem = threading.Lock()
        self.fbsem = threading.Lock()

        self.fsem.acquire()
        self.bsem.acquire()
        self.fbsem.acquire()
        self.main = threading.Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fsem.acquire()
            if self.n == 0 : return
            printFizz()
            self.main.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while True:
            self.bsem.acquire()
            if self.n == 0 : return
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fbsem.acquire()
            if self.n == 0 : return
            printFizzBuzz()
            self.main.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.main.acquire()
            if i %  3 == 0 and i % 5 == 0:
                self.fbsem.release()
            elif i % 5 == 0:
                self.bsem.release()
            elif i % 3 == 0:
                self.fsem.release()
            else:
                printNumber(i)
                self.main.release()

        self.main.acquire()
        self.n = 0
        self.fsem.release()
        self.bsem.release()
        self.fbsem.release()
        
