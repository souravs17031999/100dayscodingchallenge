# Program to add the numbers using bitwise operators
# Logic is to use half adder logic, like "&" AND operator is used for getting carry - positions where both numbers have set bits because
# only on those positions we can have carry
# and "^" XOR is useful for getting the actual sum.
# but the thing is that we actually add the carry by left shifting it by 1 in the next iteration.
# Algorithm is similar to what we usually do in normal multiplication elementry way but using bits now.

def add_bitwise(x, y):
    '''
    function :  to add the two numbers given
    x (int): first number
    y (int) : second number

    return : the result of addition of two numbers given as input to this method
    '''
    while y != 0:
        # here x is actual sum maintaining running sum, and y is bascially carry left shited by 1
        # we are doing both in parallel
        x, y = x ^ y, (x & y) << 1

    # finally x will contain the overall sum
    return x


if __name__ == '__main__':
    a, b = 15, 32
    print(add_bitwise(a, b))
