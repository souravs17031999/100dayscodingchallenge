# Program to compute min and max without using any branching , if-else,
# or any arithmetical operators.
# IDEA: Logic is to use bit wise approach, using bit level information, we have make some
# equation connecting "x" and "y" which can return which of them is min and max (separately).
# Let's understand what if (x < y), then, what will be -(x < y) = > -1 (in decimal) and
# 11111111...1111 (in binary), so if we AND this any number, then we get same number.
# so, keeping this in mind and let's say we want to compute min , that is our answer should be x,
# we can write : min(x, y) = y ^ ((x ^ y) & -(x < y)) because, ((x ^ y) & -(x < y)) will return x ^ y
# and y ^ (x ^ y) will return x.
# similarly, if we want to compute max, then if x > y, so now if x<y is false.
# Now, -(x < y) => -000000...000 => 00000.0000000
# Then, (x ^ y) & -(x < y) => x ^ y, then, x ^ (x ^ y) = > y which is maximum.

import random

def compute_min_max(x, y):

    min =  y ^ ((x ^ y) & -(x < y))
    max =  x ^ ((x ^ y) & -(x < y))

    return min, max

# For some machines, computing x < y is slower due to branching being done
# If arithmetical operators are allowed, then we can follow some different approach.
# We can use the fact that Int_MIN <= (x - y) <= Int_MAX
# min(x, y) = y + ((x - y) & ((x - y) >>(sizeof(int) * CHAR_BIT - 1)))
# max(x, y) = x - ((x - y) & ((x - y) >> (sizeof(int) * CHAR_BIT - 1)))
# This method shifts the subtraction of x, y by 31 (if size of int is 32).
# if (x - y) is negative, then (x - y) >> 31 => 1
# and if (x - y) is positive, then (x - y) >> 31 0.
# so, in min case, y + (x - y)&1 = x
# and in max case y + (x - y)&0  = y.

import sys
CHAR_BIT = 8
INT_BIT = sys.getsizeof(int())

def compute_min_max_efficient(x, y):
    min = y + ((x - y) & (x - y) >> (INT_BIT * CHAR_BIT - 1))
    max = x - ((x - y) & (x - y) >> (INT_BIT * CHAR_BIT - 1))

    return min, max

if __name__ == '__main__':

    x, y = random.randint(0, 10000), random.randint(0, 10000)
    min, max = compute_min_max(x, y)
    print(f"X : {x}, Y : {y} => Min : {min} Max : {max}")
    min, max = compute_min_max_efficient(x, y)
    print(f"X : {x}, Y : {y} => Min : {min} Max : {max}")
