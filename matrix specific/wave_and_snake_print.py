# Program for snake pattern and wave pattern printing

def snake_print(l, rows, columns):
    '''
    parameters :
    l - list of elements
    rows - number of rows
    columns - number of columns

    '''
    # logic is that if we are on even row (0, 2, 4..) then we need to increment second index and decrement when we are on odd row , keeping first index same for that sequence
    for i in range(rows):
        if i & 1 == 0:
            for j in range(columns):
                print(l[i][j], end = " ")
        if i & 1 == 1:
            for j in range(columns-1, -1, -1):
                print(l[i][j], end = " ")


def wave_print(l, rows, columns):
    '''
    parameters :
    l - list of elements
    rows - number of rows
    columns - number of columns

    '''
    # logic is that if we are on even row (0, 2, 4..) then we need to increment first index and decrement when we are on odd row , keeping second index same for that sequence
    for j in range(columns):
        if j & 1 == 0:
            for i in range(rows):
                print(l[i][j], end = " ")
        if j & 1 == 1:
            for i in range(rows-1, -1, -1):
                print(l[i][j], end = " ")

def matrix_main(l, rows, columns):
    '''
    parameters :
    l - list of elements
    rows - number of rows
    columns - number of columns

    '''
    print("printing snake pattern : ")
    snake_print(l, rows, columns)
    print()
    print("printing wave print : ")
    wave_print(l, rows, columns)


if __name__ == '__main__':
    l = []
    print(f"enter rows : ")
    rows = int(input().strip())
    print(f"enter columns : ")
    columns = int(input().strip())
    for i in range(rows):
        a = []
        for j in range(columns):
            a.append(int(input().strip()))
        l.append(a)
    print("original matrix : ")
    for i in range(rows):
        for j in range(columns):
            print(l[i][j], end = " ")
        print()
    matrix_main(l, rows, columns)
