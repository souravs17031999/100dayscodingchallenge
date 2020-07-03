# recursive implementation for computing the value of nth factorial

def fact(n):
    if n == 1:
        return 1

    return fact(n - 1) * n

if __name__ == '__main__':
    print(fact(5))        
