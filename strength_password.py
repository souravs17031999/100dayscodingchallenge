# Program to check the strength of password depending on the weights assingned in cicular order from 0-25 inclusive where we know the
# weight_a and then we need to return the strength as the sum of the weights

def get_strength(s, weight_a):
    strength = 0
    for i in s:
        temp = (ord(i) - ord('a')) + weight_a
        if temp > 25:
            temp = (temp % 25) - 1
        strength += temp
    return strength

if __name__ == '__main__':
    assert get_strength("hellomrz", 2) == 91
    assert get_strength("aaaaa", 1) == 5
    assert get_strength("hackerrank", 10) == 128
    assert get_strength("aaaaa", 0) == 0
    assert get_strength("abcde", 0) == 10
