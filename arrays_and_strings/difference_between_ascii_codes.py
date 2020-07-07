# Program to insert ascii-codes for every pair of chars for a given string.

def DiffASCII(s):
    print(s[0], end = "")
    for i in range(1, len(s)):
        print(ord(s[i]) - ord(s[i - 1]), end = "")
        print(s[i], end = "")

if __name__ == '__main__':
    s = "acb"
    DiffASCII(s)
