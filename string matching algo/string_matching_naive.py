# program to find pattern in a string commonly called as string matching algorithm but this only covers naive algorithm (inefficient)

# IDEA: logic is to keep two pointers one at text and one at pattern , increment both when a char is matched otherwise only increment text pointer and put pattern pointer back at 0 and if pattern pointer completely exhausts, then print the starting index of text pointer from where it matched.
# TIME : 0(M * (M - N - 1)), M IS TEXT LENGTH, N IS PATTERN LENGTH, GENERALISED : 0(M * N)
# SPACE : 0(1)
# FOLLOWING IS THE IDEA SHOWN IN THE CODE : 

# # TEXT :      A A B A A C A A D A A B A A B A 
#               i

# # PATTERN :   A A B A
#               j
    
# A A B A A C A A D A A B A A B A 
#   i

# A A B A
#   j
    
# A A B A A C A A D A A B A A B A 
#     i

# A A B A
#     j

# A A B A A C A A D A A B A A B A 
#       i
#                                            => complete match , print the index, then keep on moving for showing not match idea 
# A A B A
#       j    

# Resetting pointer j to 0, and i to now second window 

# A A B A A C A A D A A B A A B A 
#   i

# A A B A
# j

# A A B A A C A A D A A B A A B A 
#     i
#                                           => not matched, that means the current window is not useful, hence we discard the entire window, point i to next window, but reset j to 0.
# A A B A
#   j
    
    
# A A B A A C A A D A A B A A B A 
#     i

# A A B A
#  j
#
# AS WE CAN SEE, WE ARE RECOMPARING THE PATTERN WITH REPEATED OVERLAPPING WINDOWS, THIS ACCUNTS FOR QUADRATIC RUN TIME.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

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
