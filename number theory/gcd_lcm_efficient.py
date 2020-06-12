# program to compute gcd and lcm efficiently
# logic is to use euclid's algorithm , ex. 10, 20 -> here we take a as 10 and b as 20.
# now, first divide 20 by 10, take remainder and then again divide now by this remainder to 10 that is 0, and so on now since here, it comes as zero in only one iteration, then stop (it's stopping criteria) otherwise keep dividing by the remainder of calculate prev division.
# function to return the gcd of numbers
def gcd(x, y):
    if x == 0:
        return y
    else:
        return gcd(y % x, x)

# function to return the lcm of numbers
# here, we know that gcd * lcm = a * b (product of two numbers)
def lcm(x, y):
    if x == 0 and y == 0:
        return 0
    g = gcd(x, y)
    return x * y // g

# main function
if __name__ == '__main__':
    assert lcm(10, 20) == 20
    assert lcm(0, 10) == 0
    assert lcm(10, 0) == 0
    assert lcm(0, 0) == 0
    assert lcm(1, 1) == 1
    print(lcm(90, 2)) == 90
