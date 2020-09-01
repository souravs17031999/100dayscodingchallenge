# Program for counting the construction of the target string according to given array of strings.
# EX.
# Input :  A = ["adc", "aec", "erg"], S = "ac"
# Output : 4
# Target string can be formed in following ways :
# 1) 1st character of "adc" and the 3rd character of "adc".
# 2) 1st character of "adc" and the 3rd character of "aec".
# 3) 1st character of "aec" and the 3rd character of "adc".
# 4) 1st character of "aec" and the 3rd character of "aec".
#
# Input : A = ["afsdc", "aeeeedc", "ddegerg"], S = "ae"
# Output : 12
# ---------------------------------------------------------------------------------------------------------

cache = {}
mod = 10000007
def calculate(pos, prev, s, index):

    if pos == len(s):
        return 1

    if (pos, prev) in cache:
        return cache[(pos, prev)]

    answer = 0
    for i in range(len(index)):
        if index[i] > prev:
            answer = answer + calculate(pos + 1, index[i], s, index)

    cache[(pos, prev)] = answer

    return cache[(pos, prev)]


def count_target_string(arr, target):

    index = [[] for _ in range(26)]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            index[ord(arr[i][j]) - ord('a')].append(j + 1)

    return calculate(0, 0, target, index[0])


print(count_target_string(['abc', 'aec', 'erg'], "ac"))
