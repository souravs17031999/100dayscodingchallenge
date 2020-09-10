# Program to print the longest substring with exactly k unique characters , if more than one
# then print any one of them.

# "aabbcc", k = 1
# Max substring can be any one from {"aa" , "bb" , "cc"}.
#
# "aabbcc", k = 2
# Max substring can be any one from {"aabb" , "bbcc"}.
#
# "aabbcc", k = 3
# There are substrings with exactly 3 unique characters
# {"aabbcc" , "abbcc" , "aabbc" , "abbc" }
# Max is "aabbcc" with length 6.
#
# "aaabbb", k = 3
# There are only two unique characters, thus show error message.

# -------------------------------------------------------------------------------------------------------------------------------------
# "aabbcc", k = 1
# So, we can see what all ssubstrings we can generate :
# a, aa, aab, aabb, .....
# but the catch is to have a counter var for max len obtained so far and also if at anytime
# we found a substring with exactly k unique chars, so we can store it in a ans var.
# aa,
# If we apply this brute force, it would take O(n^2) to generate all substrings and O(n) to do a check on each one.
# Thus overall it would go O(n^3).

# Can we do better than this ?
# We will use HASHMAP (MAX 26 SIZE FOR ASSUMING ALL LOWER CASE CHARS), named as count array which updates frequency of array.
# So, we will preprocess the the whole string and fill the count array.
# We can use window sliding technique, to slide the window of size 1, to further expand the array length
# and then check if valid count array, shrink the window from left side by removing occurence of chars and increment the start pointer,
# then, we can update the window size.

# TIME : 0(N), WITH CONSTANT SPACE: 0(26)/0(1)

def isValid(count, k):
    val = 0
    for i in range(MAX_CHARS):
        if count[i] > 0:
            val += 1

    # Return true if k is greater than or equal to val
    return (k >= val)

# pseduo code

count = [0] * MAX_CHARS
for i in range(n):
        if count[ord(s[i])-ord('a')] == 0:
            u += 1
        count[ord(s[i])-ord('a')] += 1

if u < k:
        print ("Not enough unique characters")
        return

start, end = 0, 0
max_window_size = INT_MIN
count = [0] * len(count)
count[ord(s[0])-ord('a')] += 1

for i in range(1,n):
    count[ord(s[i])-ord('a')] += 1
    end += 1

    while not isValid():
        count[ord(s[curr_start])-ord('a')] -= 1
        curr_start += 1

    update the window size,
    if end-start + 1 > max_window_size:
        update the size
