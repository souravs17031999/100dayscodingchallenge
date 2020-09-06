# Program to remove common charactcers and return the concatenation of two strings with all
# uncommon charactcers.
#Input:
# 2
# aacdb
# gafd
# abcs
# cxzca
#
# Output:
# cbgf
# bsxz
#
# Explanation:
# Testcase 1:
# The common characters of s1 and s2 are: a, d.
# The uncommon characters of s1 and s2 are: c, b, g and f.
# Thus the modified string with uncommon characters concatenated is: cbgf
# -----------------------------------------------------------------------------------

#code
from sys import stdin, stdout

def remove_common(s1, s2):
    s = set(s1)
    res = []
    common = set()
    for i in s2:
        if i in s:
            common.add(i)

    for i in s1:
        if i not in common:
            res.append(i)

    for i in s2:
        if i not in common:
            res.append(i)

    if len(res) == 0:
        return str(-1)

    return "".join(res)

if __name__ == '__main__':
    t = int(stdin.readline().strip())
    for i in range(t):
        s1 = stdin.readline().strip()
        s2 = stdin.readline().strip()
        stdout.write(remove_common(s1, s2))
        stdout.write('\n')
