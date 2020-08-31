# Fast I/O   
from sys import stdin, stdout    

if __name__ == '__main__':   
    first method : input_list = list(map(int, stdin.readline().strip().split()))   or input_list = [x for x in stdin.readline().split()]  
    second method : int(stdin.readline().strip())   

    first method = stdout.write(var)  # always a string inside stdout    
    second method = stdout.write(f"{var}\n")   
    nested inputs list     
    park = []   
    for i in range(n):     
       park.append(list(map(int, stdin.readline().strip().split())))    

    third method : lines = stdin.readlines() # for more efficient I/O, load all input at once, and then loop over it.
# use lambda for short hand functions !   
# use in-built collections and itertools !   
