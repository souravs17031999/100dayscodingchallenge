# small helper functions for bitsmasking problems

# function to know whether the number given is odd or even
def isEven(x):
    return x & 1

# function to get the bits at ith position
def getBit(x, i):
    return 1 if (x & (1 << i)) > 0 else 0

# function to get the bits at ith position
def setBit(x, i):
    return (x | (1 << i))

# function to clear the bits at ith position
def clearBit(x, i):
    return (x & ~(1 << i))

# function to update the bits at ith position with the given value
def updateBit(x, i, v):
    cleared = x & ~(1 << i)
    return cleared | (v << i)

# function to clear ith bits from list
def clearBitsItoJ(x, i):
    return x & (-1 << i)

# function to clear ith to jth bits from last
def clearBitsRange(x, i, j):
    a_mask = (-1) << (j + 1)
    b_mask = (1 << i) - 1
    return x & (a_mask | b_mask)

# function to replace n bits from ith to jth by m bits 
def replaceBits(n, m, i, j):
    cleared_mask = clearBitsRange(n, i, j)
    return cleared_mask | (m << i)

if __name__ == '__main__':
    x = 15
    pos = 3
    m = 2
    n = 1
    i, j = 2, 4
    print(f"Number in binary : {bin(x)}")
    print(f"bit in {pos}th position from right : {setBit(x, pos)}")
    print(f"after bit setting at {pos}th position : {setBit(x, 1)}")
    print(f"after bit clearing at {pos}th position : {clearBit(x, 0)}")
    print(f"after bit updation at {pos}th position : {updateBit(x, 0, 0)}")
    print(f"after bit clearing from last ith at {pos}th position : {clearBitsItoJ(x, 3)}")
    print(f"after bit clearing from ith to jth at {pos}th position : {clearBitsRange(x, 3, 6)}")
    print(f"after replacing {n} by {m} from {i} to {j} : {replaceBits(n, m, i, j)}")
