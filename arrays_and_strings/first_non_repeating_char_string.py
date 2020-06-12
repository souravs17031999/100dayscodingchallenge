# program for finding first non repeating character in a given string

# IDEA: logic is that we can store frequencies of all chars in the string in a temp - count array and then simply oterate over the string and return the first index wherever we get 1 for that string frequency but in real data , it can cause problems if the string is too huge , so we can slighly modify the algorithm so that we donot go over entire string once again , but only go for count (temp) array which will ofcourse be smaller - max 256 but string size maybe millions.
import sys
# function to return index of first non repeating char in the string argument
def get_first_char(s):
    max = ord(s[0])  # ord is used to get ASCII value as temp array is based on this ascii values
    # find max value of all ASCii values
    for i in s:
        if max < ord(i):
            max = ord(i)
    # now inialize the array so that we get a array of size which includes the maxiumim element till then
    count = [[0, 0] for _ in range(max)]
    # now, we store the frequency of element
    for i in range(len(s)):
        count[ord(s[i])-1][0] += 1  # this first element is frequency
        count[ord(s[i])-1][1] = i   # this second element is position where it occured first time
    index = sys.maxsize     # so that it can work in real data practical situations
    # updating the required index of the char to be returned based on all second values in inner lists
    for i in count:
        if i[0] == 1:
            index = min(index, i[1])  # same as if index > i[1] then index = i[1]
    return index

# main function
if __name__ == '__main__':
    user_string = sys.stdin.readline().strip()
    # here , we are simply reducing the computations for irrelevant cases like what if string is empty , what if it contains only one character ?
    if len(user_string) == 0:
        print('your string is empty')
    elif len(user_string) == 1:
        print(f'first non repeating char is \'{user_string}\'')
    else:
        # call the function only for proper normal string 
        print(f'your string is {user_string}')
        index = get_first_char(user_string)
        if index == sys.maxsize:
            print('all chars are repeating')
        else:
            print(f'first non repeating char is \'{user_string[index]}\'')
            

 # if the problem asks for kth non repeating character for the string, in that case we can make two lists - one for count and one for index and then 
#  sort the index list and return the k-1 th value (if there is any).
