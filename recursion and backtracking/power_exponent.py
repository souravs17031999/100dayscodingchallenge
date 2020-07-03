# recursive implementation for computing the power of a raised to b.

def power(a, b):
    if b == 0:
        return 1

    return power(a, b - 1) * a


print(power(2, 4))
