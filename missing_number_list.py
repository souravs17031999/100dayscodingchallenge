# program to find the missing number from a list of 0-n
# IDEA: logic is to take XOR for given array , and then XOR of range 0-n, and then XOR of those two results will be the missing number.
# we can see this in this way : L = A1, A2, A3 ; A1, A2, A3, A4 -> XOR will be (A1^A1)^(A2^A2)^(A3^A3)^A4 will give us A4.
# One more logic is to use gaussian formula for summing up natural numers as n*(n+1)/2 and then take sum of given list and return difference of both.
from sys import stdin, stdout
# function for finding missing number
def find_missing_number(l):
    result = 0
    # XOR for given list
    for i in l:
        result = result ^ i
    result1 = 0
    # XOR for range 0 to n
    for i in range(0, len(l)+1):
        result1 = result1 ^ i
    # this XOR will be the result
    return result ^ result1
if __name__ == '__main__':
    #input_list = list(map(int, stdin.readline().strip().split()))
    l = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    stdout.write(str(find_missing_number(l)))
