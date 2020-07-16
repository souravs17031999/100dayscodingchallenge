# Program to compare two numbers without using any comparison operators and string functions
# # IDEA: Logic is to use XOR operators and as we know
# x ^ x = 0 and x ^ y = 1

def compare(x, y):

    return x ^ y

# if use of arithmetical operators are allowed, then we need to use
# subtract => (x - y) = 0 if EQUAL.
if __name__ == '__main__':
    x, y = 30, 10
    if not compare(x, y):
        print("EQUAL")
    else:
        print("UNEQUAL !")

    x, y = 30, 30
    if not compare(x, y):
        print("EQUAL")
    else:
        print("UNEQUAL !")
