# Program to compute the compliment of number.
# APPROACH 1:

def bin_to_dec(n):
    res = 0
    power = 0
    ptr = len(n) - 1
    while ptr > 0:
        res += int(n[ptr]) * (2 ** power)
        power += 1
        ptr -= 1

    return res

def compute_compliment(n):
    s = bin(n)[2:]
    s = list(s)
    for i in range(len(s)):
        s[i] = int(s[i]) ^ 1

    return bin_to_dec("".join(map(str, s)))

# APPROACH 2:
# Here, in this soution, we are just making another bit variable to be full of 1's upto
# the length of bits in num and then simply returning the XOR of two
# num = 5 = 101
# bit ===== 111
# Ans ==== 010 = 2
# ----- bitwise -------

def compute_compliment_bitwise(n):

    temp1 = 0
    temp2 = n
    while temp2:
        temp1 = (temp1 << 1) ^ 1
        temp2 = temp2 >> 1

    return temp1 ^ n

print(compute_compliment_bitwise(27))
