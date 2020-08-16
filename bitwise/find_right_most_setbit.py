# simple right shifting bit one by one until it hits 1, if it hits 1, then we check and return the count.
# TIME : 0(log(n)) as max digits is log2(n).

def get_right_set_bit(n):
    count = 1
    while n:
        if n & 1:
            return count
        n = n >> 1
        count += 1
