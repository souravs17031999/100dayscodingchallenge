# Program for fast multiplication using karatsuba algorithm - divide and conquer approach
# We keep dividing the numbers and solve the product recursively by making total 3 recursive calls to compute exact three products namely ac , bd, (a+b)(c+d),
# for a given number X and Y divided as a, b and c, d respectively.
# Any number can be written as X : (10^n)*ac + (10^(n/2))*(a + b)(c + d) + bd
# TIME : 0(n^1.58) which is better than traditional algorithm ((0(N^2)))


# Here, taking inputs in string would be a good idea but not a great idea !
import math

# IMplement this split method optimized way such that it splits the number at given index
# def split_at(n, mid):
#     temp = str(n)
#     print(temp, mid)
#     return int(temp[:mid]), int(temp[mid:])

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    m = min(int(math.log10(x) + 1), int(math.log10(y) + 1))
    mid = math.floor(m/2)

    a, b = split_at(x, mid)
    c, d = split_at(y, mid)

    z0 = karatsuba(b, d)
    z1 = karatsuba((a + b), (c + d))
    z2 = karatsuba(a, c)

    return z2 * pow(10, mid * 2) + (z1 - z2 - z0) * pow(10, mid) + z0

if __name__ == '__main__':
    x, y = 12345, 67899
    print(split_at(x, y))
