# program to find pattern in a string commonly called as string matching algorithm but this only covers naive algorithm (inefficient)


# IDEA: logic is to keep two pointers one at text and one at pattern , increment both when a char is matched otherwise only increment text pointer and put pattern pointer back at 0 and if pattern pointer completely exhausts, then print the starting index of text pointer from where it matched.

# function for searching the pattern wherever , any number of times occured , also accounts for overlapping substrings
def search(pattern, text):
    i, j = 0, 0   # i points to text char, and j points to pattern char
    n = len(text)
    m = len(pattern)
    flag = 0     # to keep a check if there is no pattern found
    # iterating over complete text
    while(i < n):
        # matches, then increment both
        if text[i] == pattern[j]:
            i += 1
            j += 1
        # otherwise, only increment text pointer and put pattern pointer back to 0
        else:
            i += 1
            j = 0
        # complete pattern matched
        if j == m and m != 1:
            j = 0
            i -= 1
            print(f'index found at {i-m+1}')
            flag += 1
        elif j == m and m == 1:
            j = 0
            print(f'index found at {i-m+1}')
            flag += 1
    # no match found as flag remains 0
    if(not flag):
        print('no match found !')

search('TEST', 'THIS IS A TEST TEXT')
