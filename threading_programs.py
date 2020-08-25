# Program for odd and even print numbers using two threads in python3

import threading as th
import time


event_even = th.Event()
event_odd= th.Event()

def even_function():
    for i in range(0, 30, 2):
        print("EVEN..", end = "")
        print(i)
        event_odd.set()
        event_even.clear()
        event_even.wait()
    event_odd.set()

def odd_function():
    event_odd.wait()
    for i in range(1, 30, 2):
        print("ODD..", end = "")
        print(i)
        event_even.set()
        event_odd.clear()
        event_odd.wait()
    event_even.set()




if __name__ == "__main__":
    # Odd Even Thread Application
    even = th.Thread(target=even_function, args=())
    odd = th.Thread(target=odd_function)
    even.start()
    odd.start()

    even.join()
    odd.join()

# -------------------------------------------------------------------------------------------------------------------

// C code to synchronize threads
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t* cond = NULL;

int threads;
volatile int cnt = 0;

// function to synchronize threads
void* foo(void* arg)
{
	// turn is a basically to identify a thread
	int turn = *(int*)arg;

	while (1) {
		pthread_mutex_lock(&mutex);

		// cnt is used to determne which thread should
		// enter into critical section(printf() statement)
		if (turn != cnt) {

			// put all thread except one thread in waiting state
			pthread_cond_wait(&cond[turn], &mutex);
		}

		// it's a time to print turn can have
		// values starting from 0. Hence + 1
		printf("%d ", turn + 1);

		// detemine which thread need to be scheduled now
		if (cnt < threads - 1) {
			cnt++;
		}
		else {
			cnt = 0;
		}

		// weak up next thread
		pthread_cond_signal(&cond[cnt]);
		pthread_mutex_unlock(&mutex);
	}

	return NULL;
}

// Driver code
int main()
{
	pthread_t* tid;
	volatile int i;
	int* arr;

	printf("\nEnter number of threads: ");
	scanf("%d", &threads);

	// allocate memory to cond (conditional variable),
	// thread id's and array of size threads
	cond = (pthread_cond_t*)malloc(sizeof(pthread_cond_t) * threads);
	tid = (pthread_t*)malloc(sizeof(pthread_t) * threads);
	arr = (int*)malloc(sizeof(int) * threads);

	// create threads
	for (i = 0; i < threads; i++) {
		arr[i] = i;
		pthread_create(&tid[i], NULL, foo, (void*)&arr[i]);
	}

	// waiting for thread
	for (i = 0; i < threads; i++) {
		pthread_join(tid[i], NULL);
	}

	return 0;
}

# -------------------------------------------------------------------------------------------------------
# printing sequence infinetely ....

// C code to print 1 2 3 infinitely using pthread
#include <stdio.h>
#include <pthread.h>

// Declaration of thread condition variables
pthread_cond_t cond1 =
			PTHREAD_COND_INITIALIZER;
pthread_cond_t cond2 =
			PTHREAD_COND_INITIALIZER;
pthread_cond_t cond3 =
			PTHREAD_COND_INITIALIZER;

// mutex which we are going to
// use avoid race condition.
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

// done is a global variable which decides
// which waiting thread should be scheduled
int done = 1;

// Thread function
void *foo(void *n)
{
		while(1) {

				// acquire a lock
				pthread_mutex_lock(&lock);

				if (done != (int)*(int*)n) {

						// value of done and n is not equal,
						// hold wait lock on condition variable
						if ((int)*(int*)n == 1) {
								pthread_cond_wait(&cond1, &lock);
						} else if ((int)*(int*)n == 2) {
								pthread_cond_wait(&cond2, &lock);
						}
						else {
								pthread_cond_wait(&cond3, &lock);
						}

				}
				// done is equal to n, then print n
				printf("%d ", *(int*)n);

				// Now time to schedule next thread accordingly
				// using pthread_cond_signal()
				if (done == 3) {
						done = 1;
						pthread_cond_signal(&cond1);
				}
				else if(done == 1) {
						done = 2;
						pthread_cond_signal(&cond2);
				} else if (done == 2) {
						done = 3;
						pthread_cond_signal(&cond3);
				}

				// Finally release mutex
				pthread_mutex_unlock(&lock);
		}

		return NULL;
}

// Driver code
int main()
{
		pthread_t tid1, tid2, tid3;
		int n1 = 1, n2 = 2, n3 = 3;

		// Create 3 threads
		pthread_create(&tid1, NULL, foo, (void *)&n1);
		pthread_create(&tid2, NULL, foo, (void *)&n2);
		pthread_create(&tid3, NULL, foo, (void *)&n3);

		// infinite loop to avoid exit of a program/process
		while(1);

		return 0;
}
# --------------------------------------------------------------------------------------------------------
# Program for fizzbuzz threading
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.done = False
        self.fsem = threading.Semaphore(0)
        self.bsem = threading.Semaphore(0)
        self.fbsem = threading.Semaphore(0)
        self.nsem = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fsem.acquire()
            if self.done : break
            printFizz()
            self.nsem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while True:
            self.bsem.acquire()
            if self.done : break
            printBuzz()
            self.nsem.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fbsem.acquire()
            if self.done : break
            printFizzBuzz()
            self.nsem.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.nsem.acquire()
            if i %  3 == 0 and i % 5 == 0:
                self.fbsem.release()
            elif i % 5 == 0:
                self.bsem.release()
            elif i % 3 == 0:
                self.fsem.release()
            else:
                printNumber(i)
                self.nsem.release()

        self.nsem.acquire()
        self.done = True
        self.fsem.release()
        self.bsem.release()
        self.fbsem.release()
        
