# program to check if the number is isPerfectSquare or not without use of math.sqrt
# logic is to loop over all the numbers from 1 to sqrt(n) so, it will take much lesses time than looping over n.

def isPerfectSquare(num: int) -> bool:
    # if num is 0 or 1, then it is true
    if num == 0 or num == 1:
        return 1
    i = 1
    # otherwise, loop till it becomes true (sqrt(n))
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False
print(isPerfectSquare(14))
print(isPerfectSquare(493658625628))
