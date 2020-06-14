# Program to check if solutions of linear diophantine equations possible or not ?
# Linear diophantine equations are linear polynomials in the form of a*x + b*y = c and x, y can take only integral solutions.
# Equations can be of more than two unknowns also.
# Firstly we check if solutions exist or not , if yes then what are those integers for which it holds.

from math import gcd
from sys import stdin, stdout

# Function to check if solutions exist for given values of a, b, c
# IDEA: logic is to get the gcd of a, b so that we can get a number which divides a, and b evenly and then since x and y are integers,
# so overall a*x + b*y  gets divided evenly and since a*x + b*y = c, so c also should get divided evenly by this gcd.

def check_diophantine(a, b, c):
    return (c % gcd(a, b)) == 0

# function to find exact one of the integral solutions if the solution exists
def find_diophantine(a, b, c):
    if check_diophantine(a, b, c):
        i = 0
        while i * a <= c:
            if (c - (a * i)) % b == 0:
                print("Found solution -")
                print(f"x : {i},  y : {int((c - (i * a)) / b)}")
                break
            i += 1
    else:
        print("No solution possible !")

# main driver program 
if __name__ == '__main__':
    print("Enter values of a, b, c (spaced): ")
    a, b, c = list(map(int, stdin.readline().strip().split()))
    find_diophantine(a, b, c)
