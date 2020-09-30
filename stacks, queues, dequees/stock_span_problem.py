# Program to compute span of the stocks given that stocks are values or prices given in array on nth day and
# the span is the first value on the left that is greater than or equal to the current stock price on a given day.
# SO, we have to return the indices of all the spanned element for every stock price of the array.
# IDEA: Naive solution is to iterate throught the array one by one, then for each element starting from there, going left, we check and mark
# when we encounter first majority element.
# In this way, TIME WILL BE 0(N^2) AND SPACE : 0(N)
# WE CAN DO BETTER THAN THIS , SURELY USING STACKS AS INTERMEDIATE DATA structure,
# WHAT WE CAN DO IS we can simply create a temporary window of current useful elements which are probable the spans of the current stocks
# and ignore those which are not useful in the sense that if we should not compare those element which are smaller than current element
# and only see majority element than the current element.
# So, we maintain a stack of current useful elements and pop all the not useful elements.
# TIME : 0(N), SPACE : 0(N)

# --------------------- Concise and clear code ----------------------------------------------------------------------------------------
# This problem is very similar to finding the neearest greater to the left as we are spanning to the left consecutively and stopping as soon as we find something greater
# that itself.
# So, we can apply the same logic to find the indices for the nearest greater to left, and then res[i] = i - stack[-1]
# as i is current index we are looping, then stack top is having the answer for the nearest greater to left (till where all elements are smaller than or equal to itself)

from collections import deque 
class StockSpanner:

    def __init__(self):
        self.res = []
        self.stock = []

    def compute(self):
        
        stack = deque()
        for i in range(len(self.stock)):

            while stack and self.stock[i] >= self.stock[stack[-1]]:
                stack.pop()

            if not stack:
                self.res.append(1)
            else:
                self.res.append((i - stack[-1]))

            stack.append(i)
    
    def next(self, price):
        self.stock.append(price)
        self.compute()
        return self.res[-1]
        
if __name__ == '__main__':
    
    obj = StockSpanner()
    arr = [100, 80, 60, 70, 60, 75, 85]
    for i in arr:
        print(obj.next(i))
    
    



# Alternate method but same approach :
from collections import deque

def compute_span(arr):
    n = len(arr)
    res = [0 for _ in range(n)]
    stack = deque()
    stack.append(0)
    res[0] = 1
    for i in range(1, n):

        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        res[i] = i + 1 if len(stack) <= 0 else abs(i - stack[-1])

        stack.append(i)

    return res


if __name__ == '__main__':
    arr = [10, 4, 5, 90, 120, 80]
    print(compute_span(arr))
