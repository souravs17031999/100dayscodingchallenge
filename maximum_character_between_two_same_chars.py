# program for finding maximum number of characters between two same chars
# IDEA: logic is to maintain a temporary array (i don't know why i always name it as 'count') , and then initialize it as -1 so that we know we haven't seen thay char yet and the index are based on the ASCII values. Now we traverse and we check if the char is encountered for the first time, then we set its index and if it has already been encountered, then we simply update the result of difference between current index and last index of that particular char and update our max if required.

from sys import stdin, stdout
def max_char(s):
    max_char = ord(s[0])  # ord is used to get ASCII value as temp array is based on this ascii values
    # find max value of all ASCii values
    for i in s:
        if max_char < ord(i):
            max_char = ord(i)
    # now inialize the array so that we get a array of size which includes the maxiumim element till then
    count = [-1 for _ in range(max_char)]
    # storing our max no in this variable - result_max
    result_max = count[0]
    for i in range(len(s)):
        # this will be -1 if not seen , otherwise anything but -1 if already been seen.
        first_idx = count[ord(s[i]) - 1]
        # not been seen, set its first index
        if first_idx == -1:
            count[ord(s[i]) - 1] = i
        else:
        # already seen, so simply check if we need to update our max and do if required
            result_max = max(result_max, i - first_idx - 1)
    return result_max
if __name__ == '__main__':
    s = 'abbabbbckjkjka'  # 12
    stdout.write(str(max_char(s)))
