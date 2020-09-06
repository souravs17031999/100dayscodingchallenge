# Program to print the string ignoring alternate occuring characters.
# Meaning first time we see the char, we print it, next time we see it, we don't print it.
# Again we print it, and then not print it and keep going on when seeing the same char.
# Input:
# 2
# It is a long day dear.
# Geeks for geeks
# Output:
# It sa longdy ear.
# Geks fore
# ---------------------------------------------------------------------------------------------------------------------


#code
from sys import stdin, stdout

def remove_string(s):
    res = []
    count = [0] * 256

    for i in s:
        if count[ord(i.lower())]:
            count[ord(i.lower())] = 0
        else:
            count[ord(i.lower())] = 1
            res.append(i)

    return "".join(res)


if __name__ == '__main__':

    t = int(stdin.readline().strip())
    for i in range(t):
        l = stdin.readline().strip()
        stdout.write(remove_string(l))
        stdout.write('\n')
