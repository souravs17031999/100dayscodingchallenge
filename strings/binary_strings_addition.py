# Program for adding two binary strings together without using any int() conversion
# Idea is same as was done for digit sum using arrays ,
# We add one by one from last index of both string, and take divison and modulo as our carry, result respectively.

def binary_add(s1, s2):

    max_len = max(len(s1), len(s2))
    s1 = s1.zfill(max_len)
    s2 = s2.zfill(max_len)

    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if s1[i] == '1' else 0
        r += 1 if s2[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry !=0 : result = '1' + result
    return result.zfill(max_len)


print(binary_add('1101', '100'))
