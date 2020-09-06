# Program to compute if given string is palindrome or not.
# So, like "geeksforgeeks" is not palindrome.
# and "geeksogeeks" is palindrome.
# ------------------------------------------------------------------
# Now, for a string to be palindrome, it should be same spelled backwards
# and forwards.
# So, for spelling same, it should be the case that all the chars from start
# and last should match while traversing using two pointers,
# and if at any point, it is not same then that is not a palindrome.
# --------------------------------------------------------------------
# NOTE : It is guaranteed that input string is not containing any other item
# that ascii_letters (lowercase).
# If case are not same, then we can just modify one line and make both cases same while comparing.
# If there more chars like whitespace and other chars, then we can surely skip those and only check for real valid chars.
# ----------------------------------------------------------------------
# TIME : 0(S), S is length of string.

def check_palindrome(s):
    start, end = 0, len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1
    return True

# If added constraints, that we need to ignore spaced and other symbols except numbers and whitespaces, even ignore the cases also.

#code
from sys import stdin, stdout

def check_palindrome(s):
    start, end = 0, len(s) - 1
    while start <= end:

        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue

        if s[start].lower() != s[end].lower():
            return "NO"

        start += 1
        end -= 1
    return "YES"

if __name__ == '__main__':
    assert check_palindrome("geeksforgeeks") == False
    assert check_palindrome("geeksoskeeg") == True
