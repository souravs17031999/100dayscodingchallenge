# program to print pascal's traingle and return one row if prompted to do so

# import from my own library for efficieny purposes
from mathemagica import mathemagica as m

# function to print pascal_triangle
def pascal_triangle_print(n, ret):
    # print and return from here if only row is to be printed
    if (ret == 1):
        for i in range(n):
            for j in range(i + 1):
                if i == n - 1:
                    print(f'{m.binom(i, j)}', end = " ")
        return
    # from here whole triangle is printed
    # printing traingle using each binomial coefficients calculation
    print('printing whole traiangle...')
    for i in range(n):
        # printing spaces
        for j in range(n-i-1):
            print(' ', end = " ")
        # printing digits for that row
        for j in range(i + 1):
                print(f'{m.binom(i, j)}  ', end = " ")
        print()


# main function
if __name__ == '__main__':
    print('Wanna print the whole traiangle or just a row : ? press 0 for former and 1 for latter')
    t = int(input())
    print('enter the number of rows to be printed:')
    n = int(input())
    pascal_triangle_print(n, t)
