# Program to compute exponentiation efficiently
# compute a raise to power b most efficient way using bitwise logic
# IDEA: firstly, we note that if we normally multiply "a" , "b" number of times, then it takes 0(N) time which is not optimal,
# so, what we use is bit level information for "b" and use it to multiply "a" only when there is set bit "1" in "b" which reduces the
# computations of multiplcations at most log(N) times.
# Time : 0(log(N)), SPACE : 0(1)

def expo(a, n):
    ans = 1
    while n > 0:
        if n & 1:
            ans *= a

        a *= a
        n = n >> 1

    return ans

if __name__ == '__main__':
    assert expo(2, 4) == 16
    assert expo(4, 4) == 256
    assert expo(3, 5) == 243
    assert expo(5, 3) == 125
    assert expo(5, 1) == 5
    assert expo(5, 0) == 1
