# program to reverse the input list word by word given each word is separated by a single space and no leading / trailing spaces exist.
# logic is to first reverse the complete list and then reverse the word by word by finding positions
# of start and end indices of each word
# say, a list -> ['t', 'h', 'e', ' ', 's', 'k', 'y'] , so reversing it will look like : ['y', 'k', 's', ' ', 'e', 'h', 't']
# now, reversing it word by word will look like : ['s', 'k', 'y', ' ', 't', 'h', 'e']

# function to reverse the given list/part of list
def reverse(l, start, end):
    # move start and end using two pointers technique and keep swapping it until the middle of list
    while start < end:
        l[start], l[end] = l[end], l[start]
        start, end = start + 1, end - 1

# function to reverse the complete list of words
def reverseWords(l):
    start = end = 0
    n = len(l)
    # iterating the complete list
    while start < n:
        # finding the position of pointer end index
        while end < n and l[end] != ' ':
            end += 1
        reverse(l, start, end - 1)
        # always start will start from just next to end pointer
        start = end + 1
        # now, after detecting space, then move to just next char so that it will detect next char
        end += 1

# main function
if __name__ == '__main__':
    l = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    print(l)
    n = len(l)
    # reversing complete list
    reverse(l, 0, n-1)
    # reverse word by word
    reverseWords(l)
    print(l)
