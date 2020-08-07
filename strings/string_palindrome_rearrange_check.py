# Program to compute if palindrome can be formed by rearranging the chars of the string.
# One thing to note is that we donnot need to actually rearrange the letters and then check
# for palindrome, because it would be then too much time and inefficient.
# So, what can we do ?
# ----------------------------------------------------------------------------------------
# So, one thing to note is that for a string to be palindrome there is this condition that
# chars should match from start and back (spelled same from and to), but since this is not
# in order and so what we can do is to observe that for the above said condition to be
# true, we need to be able to have even counts of all chars except only one char count.
# That means, only one char should be odd count and all others should be even, then only
# they can be arranged in the fashion such that they can be spelled forward and backwards
# same. If we find any such odd char count more than once, then obsiously its n't
# palindrome.
# ----------------------------------------------------------------------------------------
# Time : 0(S), space : 0(256) (constant space)
# Since, we are considering all the ascii chars, so 256 values.
# ----------------------------------------------------------------------------------------

def palindrome_check_rearr(s):
    count = [0] * 256
    odd = 0
    for i in range(len(s)):
        count[ord(s[i])] += 1

    for i in range(256):
        if count[i] & 1:
            odd += 1
        if odd > 1:
            return False

    return True

if __name__ == '__main__':
    assert palindrome_check_rearr("geeksforgeeks") == False
    assert palindrome_check_rearr("geeksogeeks") == True
