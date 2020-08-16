# Program for computing minimum operations required from moving 0 to N.
# We are allowed to use two operations :
# 1. Add 1 to the number
# 2. Double the number
# ---------------------------------------------------------------------------
# One of the observation is that minimum operations required from 0 -> N will be same as N -> 0.
# So, we can basically move from N -> 0, and divide and subtract (instead of add and multiply as from  0-> N).
# Now, we can think that if the number is even, then divide by 2, but if the number is odd, then we can subtract by 1 unit.
# In this way min number of operations are counted .
# ----------------------------------------------------------------------------
# TIME : 0(min_operations)

def compute_min_opr(N):
    count = 0
    while N:
        if N & 1:
            N -= 1
        else:
            N = N // 2
        count += 1
    return count

if __name__ == '__main__':
    print(compute_min_opr(7))
