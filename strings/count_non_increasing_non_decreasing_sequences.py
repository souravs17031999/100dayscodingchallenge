"""
Given a string consisting of lowercase letters 
count the number of non-increasing and non-decreasing sequences in the input


Sample Input :gfcbdhdd
Output :3(gfcb | dh | dd)


Approach :)
At start we consider the sequence type as none and will define the type of 
sequence(whether it’s non-increasing or non-decreasing)based on first two 
characters and for further characters we can define the sequence based on 
previous character we’ve seen.

We define sequence types using numbers as
increasing sequence with 1
decreasing sequence with -1
same character with 0

while traversing through the string if we found that the current character is 
not obeying the previous characters sequence then make the sequence type 
as none and check for the sequence type from current character onwards. 

We will increase the number of sequence types whenever sequence becomes none.
"""
def getParts(s):
    if(not s):
        return 0
    count = 0
    seq = None
    index = 0
    n = len(s)
    prev = ''
    curr = ''
    while index < n:
        if(seq is None):
            #Getting the new sequence type and 
            #increasing the count
            count += 1
            prev = s[index]
            index += 1
            if(index >= n):
                return count
            curr = s[index]
            if(ord(curr) > ord(prev)):
                seq = 1
            elif(ord(curr) == ord(prev)):
                seq = 0
            else:
                seq = -1
        curr = s[index]
        if(ord(curr) >= ord(prev) and (seq == 1 or seq == 0)):
            if(ord(curr) > ord(prev)):
                seq = 1
            prev = curr
            index += 1
        elif(ord(curr) <= ord(prev) and (seq == -1 or seq == 0)):
            if(ord(curr) < ord(prev)):
                seq = -1
            prev = curr
            index += 1
        else:
            seq = None
    return count
#Driver Code for tesing
print("gfcbdhdd", getParts("gfcbdhdd"))
print("ffdhbbbdeeggbb", getParts('ffdhbbbdeeggbb'))
print("aabccad", getParts("aabccad"))
