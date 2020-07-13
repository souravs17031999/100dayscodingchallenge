# In his contest he gave the contestants many different pairs of numbers. Each number is made from
# digits 0 or 1. The contestants should write a new number corresponding to the given pair of
# numbers. The rule is simple: The i-th digit of the answer is 1 if and only if the i-th digit of
# the two given numbers differ. In the other case the i-th digit of the answer is 0.

# Program for giving output on the basis of above description, giving two numbers as input.

def UltraString(s1, s2):
    for i in range(len(s1)):
        print(ord(s1[i]) ^ ord(s2[i]), end = "")

if __name__ == '__main__':
    s1, s2 = "10111", "10000"
    UltraString(s1, s2)
