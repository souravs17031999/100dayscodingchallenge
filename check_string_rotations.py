# program to check if the strings are rotations of each other or not

# IDEA: first logic comes to mind is to check if for every possible one unit shifts , if we can reach the other string, then we can say they are rotations.
# Next approach would be that we can make a copy of string and concatenate it with first string, then check if second string occurs in it, if it has to be rotated, then it must be occuring in some part (substring) of the first string.
# Both of the above approach will take 0(N*N), where N lengths of two strings and 0(N) space.
# EDIT : OVERALL WE CAN CHOOSE KMP VS BOYER MOORE FOR string matching step done after concatenation, KMP is best suited for short sequences 
# and Boyer moore is best suited for large sequences , one of which when chosen will bring the overall complexity as 0(N) unlike previously 
# which was 0(N*N).
def rotate_check(str1, str2):
    str_length2 = len(str1)
    str_length1 = len(str2)
    # check for length
    if str_length1 == str_length2:
        # check for similarity
        if str1 == str2:
            return 1
        # otherwise, make a copy and then check if string 2 occurs in string 1
        temp_string = str1 + str1
        # This is the bottleneck of the problem, so we can apply KMP matcher to reduce the overall complexity to 0(N).
        if str2 in temp_string:
            return 1
        else:
            return 0
    else:
        return 0

if __name__ == '__main__':
    assert rotate_check("ABCD", "CDAB") == True
    assert rotate_check("ABACD", "CDABA") == True
    assert rotate_check("AAAA", "AAAA") == True
    assert rotate_check("AACD", "ACDA") == True
    assert rotate_check("AABAA", "AAAAB") == True
