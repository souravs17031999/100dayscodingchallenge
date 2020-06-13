# Program for finding gcd for array of numbers
# gcd(a, b, c) = gcd(a, gcd(b, c))  = gcd(gcd(a, b), c) = gcd(gcd(a, c), b)

def gcd_extend(a, b):
    return a if b == 0 else gcd_extend(b, a % b)


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 16, 40]
    gcd = gcd_extend(arr[0], arr[1])
    for i in arr:
        gcd = gcd_extend(gcd, i)

    print(gcd)
