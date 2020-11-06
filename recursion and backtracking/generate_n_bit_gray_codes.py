# Program for generating n - bit gray codes.
# Examples:
#
# Input: N = 2
# Output: 00 01 11 10
#
# Input: N = 3
# Output: 000 001 011 010 110 111 101 100
# --------------------------------------------------------------------------------------------------------------
# If we observe carefully, then we can see, that we can actually generate "N" bit gray code using "N-1" gray codes.
# Let's say,
# For 3 bit code :
# L1 = {00, 01, 11, 10} (List of 2-bit Gray Codes)
# L2 = {10, 11, 01, 00} (Reverse of L1)
# Prefix all entries of L1 with ‘0’, L1 becomes {000, 001, 011, 010}
# Prefix all entries of L2 with ‘1’, L2 becomes {110, 111, 101, 100}
# Concatenate L1 and L2, we get {000, 001, 011, 010, 110, 111, 101, 100}
# ---------------------------------------------------------------------------------------------------------------
# But it will take exponential time to generate all the combinations.
# Alternate and more concise way for doing this will be using recursion with same asymtodic complexity of 0(2 ^ (N)).
# So, we can think about base cases :
# CASE 1 : N <= 0 : return {"0"}
# CASE 2 : N == 1 : return {"0", "1"}
# Otherwise we have to append "0" to first half and then "1" to second half reversed way.
# --------------------------------------------------------------------------------------------------------------

def generate_n_bits(N):

    if N <= 0:
        return ["0"]

    if N == 1:
        return ["0", "1"]

    temp_list = generate_n_bits(N - 1)
    res = []
    for i in range(0, len(temp_list)):
        res.append("0" + temp_list[i])

    for i in range(len(temp_list) - 1, -1, -1):
        res.append("1" + temp_list[i])

    return res

res = generate_n_bits(3)

# Backtracking approach : 

def generate_n_bits(res, n, num):

    if n == 0:
        res.append(num[0])
        return

    generate_n_bits(res, n - 1, num)
    num[0] = num[0] ^ (1 << (n - 1))

    generate_n_bits(res, n - 1, num)

def gray_codes(n):

    res = []
    num = [0]

    generate_n_bits(res, n, num)

    return res
