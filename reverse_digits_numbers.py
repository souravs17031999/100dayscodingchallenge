# program to reverse the integer keeping overflow in mind
# logic is to keep a track of all remainders and use following formula like - result = result * 10 + remainder to combine the complete inverse digits
# and keep reducing the number itself by taking in account of division by 10
from sys import maxsize, stdin, stdout
# function to reverse the integer
def reverse(self, x: int) -> int:
    # initialize the result
    result = 0
    # we need to account for +ve and -ve numbers  , so keeping +1 for +ve , -1 for -ve numbers.
    flag = 1
    if x < 0:
        flag = -1
        x = flag * x
    if x % 10 == x:
        return flag * x
    while(x >= 1):
        remainder = x % 10
        x = x // 10
        result = result * 10 + remainder
    return flag * result if result < maxsize else 0
