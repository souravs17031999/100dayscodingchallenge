# program to count set ("1") bits for an integer
# IDEA: first naive logic is to simply go over each bit and check if it is set or not which on worst case takes 0(N) time complexity.
# Second faster method is to use Brian Kernighan’s Algorithm : it basically says to AND two consecutive decreasing numbers starting from where the number was given and in every iteration it removes set bits from end, so effectively we can count how many iterations, that many set bits are there.
# This takes theta(no. of set bits) but then in worst case, every bit is set, so 0(lg(n))
def count_bits(x):
    count = 0
    while (x > 0):
        x = x & (x - 1)
        count += 1
    return count

# another method using some preprocessing using hash table (lookup table) taking 0(1) time ,
BitsSetTable256 = [0] * 256

def initialize():

    # To initially generate the
    # table algorithmically
    BitsSetTable256[0] = 0
    for i in range(256):
        BitsSetTable256[i] = (i & 1) + BitsSetTable256[i // 2]

def countSetBits(n):
    initialize()
    return (BitsSetTable256[n & 0xff] +
            BitsSetTable256[(n >> 8) & 0xff] +
            BitsSetTable256[(n >> 16) & 0xff] +
            BitsSetTable256[n >> 24])


# Another simple method but good for average inputs
print(bin(N).count('1'))

if __name__ == '__main__':
    print(count_bits(13))
    print(countSetBits(13))
