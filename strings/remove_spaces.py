# Program to remove spaces from the given string and return the modified string.

#code
from sys import stdin, stdout 
def remove_space(s, n):
    
    if n == 0:
        return ""
    
    ptr = 0
    while s[ptr] == " ":
        ptr += 1
    
    res = ""
    for i in range(ptr, n):
        if s[i] == " ":
            continue 
        else:
            res += s[i] # more efficient could be : res = "".join(res, s[i])
    
    return res
    

if __name__ == '__main__':
    t = int(stdin.readline().strip())
    for i in range(t):
        s = stdin.readline().strip()
        n = len(s)
        stdout.write(remove_space(s, n))
        stdout.write("\n")
    
