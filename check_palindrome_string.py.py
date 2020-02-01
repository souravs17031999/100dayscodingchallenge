# Program to check whether string is a valid palindrome, ignoring any other character than alphanumeric, and ignoring cases.
# Logic is to simply use two pointer technique, ignoring any non valid character , only comparing alnum chars , and returning true or false.
# Time complexity is 0(N) and space complexity is 0(1)
def valid_palindrome(s):
    # assuming empty string is valid palindrome
    if len(s) == 0:
        return True
    # assinging two pointers for start and end variables
    start = 0
    end = len(s) - 1
    # traversing the string from both end
    while start < end:
        # ignore the invalid char from start
        if not s[start].isalnum():
            start += 1
        # ignore the invalid char from end
        elif not s[end].isalnum():
            end -= 1
        # now compare valid chars
        else:
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
    # every valid char is same, from both sides, thereby returning True at this point
    return True

# main function
if __name__ == '__main__':
    assert valid_palindrome("race a car") == False
    assert valid_palindrome("A man, a plan, a canal: Panama") == True
    assert valid_palindrome("") == True
    assert valid_palindrome("A") == True
