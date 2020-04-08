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
