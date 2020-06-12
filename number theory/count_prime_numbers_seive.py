# Program to return count of prime numbers in the given range of queries randomly selected as [a, b]
# IDEA: So, naive solution will be to iterate over the number N times for each number to check whether it's prime or not from a to b which will take
# (b - a) * N time but we can use prime seive to reduce the complexity.
# Now, we use prime seive to precompute the prime numbers beforehand for max range given in problem (here 10^6), and then
# maintain a cummulative prefix sum array where we simply add up the values of its previous value with prime number array value so that it will contain
# sum of count of prime numbers existing till that particular index (as prime number array contains 1's and 0's to mark prime or not so, when we add up
# we get count of the prime numbers till that index in the cummulative sum array)
# Time : 0(Q + N*log(log(N))) where Q is no.of range queries and N is MAX_SIZE , so it's approximately linear , SPACE : 0(MAX_SIZE)
# Space can be optimized more though using segmented seive

from sys import stdin, stdout

MAX_SIZE = 100000

def prime_seive():
    # list of all numbers
    prime = [1 for _ in range(MAX_SIZE + 1)]
    i = 2
    # going from 2 to sqrt(n)
    while(i * i <= MAX_SIZE):
        # if found prime, then mark all multiples as composite
        if prime[i]:
            # starting with i * i (prime numbers' square)
            for j in range(i * i, MAX_SIZE + 1, i):
                prime[j] = 0
        i += 1

    # # printing the prime numbers marked as True
    # for i in range(2, n + 1):
    #     if prime[i]:
    #         print(i, end= " ")
    prime[0], prime[1] = 0, 0
    # print(prime)

    # constructing cummulative sum array
    cum_sum = [0 for _ in range(MAX_SIZE + 1)]
    for i in range(1, len(cum_sum)):
        cum_sum[i] = cum_sum[i - 1] + prime[i]

    # print(cum_sum)
    return cum_sum

if __name__ == '__main__':
    cum_sum = prime_seive()
    t = int(stdin.readline().strip())
    # iterating over range input queries gives as a b as in [a, b] 
    while (t):
        a, b = list(map(int, stdin.readline().strip().split()))
        print(cum_sum[b] - cum_sum[a - 1])
        t -= 1
