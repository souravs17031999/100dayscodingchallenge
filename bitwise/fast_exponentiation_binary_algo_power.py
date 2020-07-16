# Program to compute exponentiation efficiently
# compute a raise to power b most efficient way using bitwise logic
# IDEA: firstly, we note that if we normally multiply "a" , "b" number of times, then it takes 0(N) time which is not optimal,
# so, what we use is bit level information for "b" and use it to multiply "a" only when there is set bit "1" in "b" which reduces the
# computations of multiplcations at most log(N) times.
# Time : 0(log(N)), SPACE : 0(1), WHERE N IS EXPONENT.

def expo(a, n):
    ans = 1
    while n > 0:
        if n & 1:
            ans *= a

        a *= a
        n = n >> 1

    return ans

# here x, n = > a, b
def compute_power(x: float, n: int) -> float:
    if n > 0:
        return float('%.5f'%(expo(x, n)))
    else:
        return float('%.5f'%(1 / expo(x, -n)))

if __name__ == '__main__':
    print(compute_power(2.00000, 2))
    # assert expo(2, 4) == 16
    # assert expo(4, 4) == 256
    # assert expo(3, 5) == 243
    # assert expo(5, 3) == 125
    # assert expo(5, 1) == 5
    # assert expo(5, 0) == 1
    #
