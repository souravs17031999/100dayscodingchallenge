# program to check if two strings are anagram or not.
# first logic is we can simply sort the strings and compare them
# second optimized version is to count all the characters frequencies and then
# comprare both dictioneries tracking occurence of all chars whose implementation
# is below

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


if __name__ == '__main__':
    print(Anagram('SILENT', 'LISTEN'))
