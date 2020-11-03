# TIPS :
## General :
* Modify the basic structure and improve efficiency.   
* use combination of then ds along with given some other ds.   
* Two common uses for stacks are: parsing (like in this problem) and tree or graph traversal (like depth-first traversal)   

## Stacks :
* Whenever some range/span on array based question is asked and complexity is 0(N^2), then we need to use some kind of stack based technique.
* There are four techniques which are generally useful :   
* NEAREST greater to right (NGR)  
* NEAREST greater to left (NGL)  
* NEAREST smalller to right (NSR) 
* NEAREST smaller to left (NSL)   
* Logic is same for all four above as in we need to use stack for the processing and maintain only useful element in the stack and pop out all not useful elements.
* When for right, fill in from right, when for left, fill in from left.    

> Template for (NGL)/(NGR)/(NSR)/(NSL) :     
* NGR/NGL : 
```  
from collections import deque 
def NGR(arr, n):
    output = [-1] * n
    stack = deque()
    
    for i in range(n - 1, -1, -1):  # for i in range(n) => for NGL, just fill from left, no other changes
        
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if not stack:
            output[i] = -1
        else:
            output[i] = stack[-1]
        
        stack.append(arr[i])
    
    print(output)

```  
* NSR/NSL :   
```   
from collections import deque 
def NSR(arr, n):
    output = [-1] * n
    stack = deque()
    
    for i in range(n-1, -1, -1):  # for i in range(n) => NSL, just fill from left, no other changes 
        
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        if not stack:
            output[i] = -1
        else:
            output[i] = stack[-1]
        
        stack.append(arr[i])
    
    print(output)

```  
