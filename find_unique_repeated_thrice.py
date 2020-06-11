# program to find unique number in a array where every element is repeated thrice except one
# IDEA: Naive solution is to use sorting and check which one is non repeating, then one optimized time solution is to use hashing and keep counter for
# occurences and check whose count is only "1".
# Most efficient logic is to observe that the numbers will be either of form 3N or 3N + 1 and that means if converted to binary , then also
# the bits will be in the either of the two form.
# Now, we can extract one by one bits and take sum of those bits and store in a separate array of max size 64 bits, and since
# these sums are also of the form 3N or 3N + 1 , when we will take modulus of 3 , then one that unique number will give remainder "1" (3N + 1)
# and all others will be "0" (3N form).
# The final remainder of the modulus in the array will be the number when converted to decimal.
# TIME : 0(N), SPACE : 0(1)

def find_unique(arr):
    # using fixed sized arrays
    count = [0 for _ in range(64)]

    # iterating over array containing number
    n = len(arr)
    for i in range(n):
        j = 0
        # for every number, we update count array using running sum
        # overwriting older bits by adding new bits of next number
        while arr[i] > 0:
            count[j] += arr[i] & 1  # extract last bit
            j += 1
            arr[i] = arr[i] >> 1;   # right shifting by 1 bit every time

    ans = 0   # this will contain our number in decimal form
    p = 1
    # converting our binary answer (in the count array) into decimal
    for i in range(len(count)):
        count[i] = count[i] % 3
        ans += count[i] * p
        p *= 2

    return ans

# THERE CAN BE ONE MORE LOGIC IN THE MATHEMATICAL EQUATION FORM :
# Mathematical Equation = ( 3*(a+b+c+d) – (a + a + a + b + b + b + c + c + c + d) ) / 2
# Mathematical Equation = ( 3*(a+b+c+d) – (a + a + a + b + b + b + c + c + c + d) ) / 2
# CODE : Mathematical Equation = ( 3*(a+b+c+d) – (a + a + a + b + b + b + c + c + c + d) ) / 2
# Can be acheived using sets() in python


if __name__ == '__main__':
    assert find_unique([3, 3, 2, 1, 1, 1, 3]) == 2
    assert find_unique([2, 2, 2, 1, 1, 1, 3]) == 3
