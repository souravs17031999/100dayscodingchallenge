def gcd(x, y):
    if x == 0:
        return y
    else:
        return gcd(y % x, x)

def lcm(x, y):
    if x == 0 and y == 0:
        return 0
    g = gcd(x, y)
    return x * y // g
if __name__ == '__main__':
    assert lcm(10, 20) == 20
    assert lcm(0, 10) == 0
    assert lcm(10, 0) == 0
    assert lcm(0, 0) == 0
    assert lcm(1, 1) == 1
    print(lcm(90, 2)) == 90
