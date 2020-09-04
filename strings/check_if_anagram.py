# program to check if two strings are anagram or not.
# first logic is we can simply sort the strings and compare them
# ------------------------------------------------------------------------------------------------------------
# second optimized version is to count all the characters frequencies and then
# comprare both dictioneries tracking occurence of all chars whose implementation
# is below
# -----------------------------------------------------------------------------------------------------------------
# Other approach could be and would be more good for bigger strings : make a count dict of 26 chars (givent that input consists of lowercase letters)
# and if any char's count doesn't match, then simply return False.
# Also, one more optimization could be to return false early when the length of strings don't match.
# --------------------------------------------------------------------------------------------------------------------
# -------------x-----------------------x---------------------------------------------------------------------x-------ss
# How about reducing space it to 0(1), can we do ?
# Yes, we can apply XOR trick and check whether after doing XOR of both strings, if res = 0, then it is anagram otherwise not.
# CAREFUL : NO, WE CAN'T DO THIS AS "aabb" and "ccdd" will return XOR = 0, but obviosuly this is not the case.
# ---------------------------------------------------------------------------------------------------------------------
# BTW, WE HAVE ALREADY IN METHOD 3, REDUCED THE SPACE : 0(1) WITH TIME : 0(N)

# METHOD 2 :
def isAnagram(s1, s2):
    count_s1 = {}
    count_s2 = {}
    for i in s1:
        if i in count_s1:
            count_s1[i] += 1
        else:
            count_s1[i] = 0

    for i in s2:
        if i in count_s2:
            count_s2[i] += 1
        else:
            count_s2[i] = 0

    return count_s1 == count_s2

# this code takes 0(N) complexity, overall less than previous one.
def Anagram(s1, s2):
    count = {}
    for i in range(len(s1)):
        if s1[i] in count:
            count[s1[i]] += 1
        else:
            count[s1[i]] = 1
    print(count)
    for i in range(len(s2)):
        if s2[i] in count:
            count[s2[i]] -= 1
        else:
            count[s2[i]] = 1
    print(count)
    for i in count.values():
        if i:
            return "NOPE"
    return "YES !!"


# METHOD 3:
# WE CAN OPTIMIZE MORE BY JUST TAKING SINGLE COUNT ARRAY / DICT, AND INCREMENTING AND DECREMENTING THE COUNT WHILE TRAVERSING ON BOTH STRINGS.
# WHEN SEEING A CHAR, INCREMENT THE CHAR, ....
from sys import stdin, stdout

def main(l):

    first, second = l[0], l[1]

    if len(first) != len(second):
        return False

    first_dict = [0] * 26
    second_dict = [0] * 26
    for i in first:
        first_dict[ord(i) - ord('a')] += 1

    for i in second:
        second_dict[ord(i) - ord('a')] += 1

    for i in range(26):
        if first_dict[i] != second_dict[i]:
            return False

    return True


if __name__ == '__main__':
    print(Anagram('SILENT', 'LISTEN'))
