# Program to generate prime numbers less than or equal to n , most efficient way - prime seive of erastothenes
# Simply naive solution will take 0(N^2) for generating prime numbers till n
# Simple optimization is just to calculate for every number, only go till sqrt(that number),
# this wil reduce computations till 0(N^1.5) but not much optimal

# IDEA:  Logic is to start with having a list of all numbers from 0 to n , where each is marked to be True for prime numbers,
# Then, we start with first prime (iniitally with 2) and then mark all of its multiples as composite (FALSE), then
# We keep on doing this until we marked all of the mulitples of prime numbers in the order of sqrt (n) of given number n.
# That means left numbers now, which is marked True is list of prime numbers as required.

# First opimization is that we donot need to go over complete list of numbers (till n), but we can just go till sqrt(n) as divisors occur in pairs.
# Second opimization is that when we mark multiples of prime numbers, then we start off with directly the square(prime number) as
# others before that are already marked by some prime number less than current prime number.
# TIME : 0(N*log(log(N))), SPACE : O(N)


def prime_seive(n):
    # list of all numbers
    prime = [True for _ in range(n + 1)]
    i = 2
    # going from 2 to sqrt(n)
    while(i * i <= n):
        # if found prime, then mark all multiples as composite
        if prime[i]:
            # starting with i * i (prime numbers' square)
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1

    # printing the prime numbers marked as True
    for i in range(2, n + 1):
        if prime[i]:
            print(i, end= " ")

## WE CAN DO ONE MORE OPTIMIZATIONS, BASED ON PROPERTY THAT ALL EVEN NUMBERS ARE NOT PRIME,
# SO, WE NEED NOT CHECK FOR EVEN AS 2 WILL ALWAYS BE DIVISOR OF ANY EVEN NUMBER, SO, ONLY CHECK ODD NUMBERS.

# def prime_optimized(n):
#     prime = [True if i & 1 else False for i in range(n + 1)]
#     i = 3
#     while(i * i <= n):
#         if prime[i]:
#             for j in range(i * i, n + 1, i):
#                 prime[j] = False
#         i += 2
#     prime[2] = 1
#     prime[0], prime[1] = 0, 0

if __name__ == '__main__':
    prime_seive(100)
    # output : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
