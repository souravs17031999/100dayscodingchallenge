# recursive implementation for summing up the natural numbers to n

def sum_natural(x):
    if x == 1:
        return 1

    return sum_natural(x - 1) + x

if __name__ == '__main__':
    print(sum_natural(5))
