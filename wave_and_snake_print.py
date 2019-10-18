def snake_print(l, n):
    for i in range(n):
        if i & 1 == 0:
            for j in range(n):
                print(l[i][j], end = " ")
        if i & 1 == 1:
            for j in range(n-1, -1, -1):
                print(l[i][j], end = " ")


def wave_print(l, n):
    for j in range(n):
        if j & 1 == 0:
            for i in range(n):
                print(l[i][j], end = " ")
        if j & 1 == 1:
            for i in range(n-1, -1, -1):
                print(l[i][j], end = " ")

def matrix_main(l, n):
    print("printing snake pattern : ")
    snake_print(l, n)
    print()
    print("printing wave print : ")
    wave_print(l, n)


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
    print(l)
    matrix_main(l, rows)
