# Program to remove all duplicates from the given string.
# There are various methods to solve it.
# We can use sorting and then one by one remove all but one.
# -----------------------------------------------------------------------------------------------------------------
# Another method can be to use HashMap and print out all occurence exacly one time.
# -----------------------------------------------------------------------------------------------------------------
# Above two methods can cause ordering of the given string to be not same.

# For keeping ordering same, we can use OrderedDict in Python to maintain the insertion order
# of dictionery.
# -------------------------------------------------------------------------------------------------------------------------------------
# Can we do it in TIME : 0(N) AND SPACE : 0(1) with maintained ordering other than using OrderedDict?
# Yes, we can do it with slight modifications in the HASHMAP METHOD :
# In this we donot prefill the count hashmap instead, we go one by one in the input string and check first if it has occured already in the
# first place, then copy that into the next valid position in the string (pointer poiting to next valid pos from start....)
# and move on, if it has already occured then do nothing.
# in this way, we have modified string in-place and print the result like : string[:idx]
# --------------------------------------------------------------------------------------------------------------------------------

# METHOD 2 (HASHMAP) :
#code
from sys import stdin, stdout

def remove_dup(s):

    count = [0] * 256
    for i in s:
        count[s[i]] += 1

    for i in range(256):
        if count[i]:
            stdout.write(chr(i))

    stdout.write('\n')

if __name__ == '__main__':

    t = int(stdin.readline().strip())
    for i in range(t):
        remove_dup(stdin.readline().strip())

# --------------------------------------------------------------------------------------------------------------------------

# METHOD 3 (OrderedDict) :
#code
from sys import stdin, stdout
from collections import OrderedDict

def remove_dup(s):

    count = OrderedDict()

    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in count:
        stdout.write(i)

    stdout.write('\n')

# -----------------------------------------------------------------------------------------------------------------------
# METHOD 4 : IN-PLACE MODIFIED HashMap METHOD :
def remove_dup(s):

    s = list(s)
    count = [0] * 256
    idx = 0
    for i in s:
        if count[ord(i)] == 0:
            s[idx] = i
            idx += 1
            count[ord(i)] = 1

    stdout.write("".join(s)[:idx])
    stdout.write('\n')  


if __name__ == '__main__':

    t = int(stdin.readline().strip())
    for i in range(t):
        remove_dup(stdin.readline().strip())
