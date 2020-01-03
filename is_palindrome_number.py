# program to check if a given number is palindrome is not
# logic is to compute the reversed part of second half only while going through the digits and compare it with the first half
# another approach is to convert it into str and then simply reverse and compare it but it will take extra space for string
# log(x) base 10 where x is no of digits 
def check(n):
    # if number is -ve, then it is obviously not a palindrome
    if n < 0:
        return 0
    # if number is zero, then it is a palindrome
    if not n:
        return 1
    # if n is a single digit number, then it is a palindrome
    if 1 < n < 9:
        return 1
    # if numbers are of form 10, 100, 200, 1000 etc.., then it can't be palindrome
    if not n % 10:
        return 0
    # for others
    result = 0
    # going for half of the digits and computing the reverse of those half and then comparing the first half with that reversed second half
    while result < n:
        rem = n % 10
        result = result * 10 + rem
        n = n // 10
    # after this, n will be contain first half and result (reversed part) will contain second half
    return n == result or n == result // 10

if __name__ == '__main__':
    print(check(20))
    # for i in random.sample([random.randint(0, 1000000) for i in range(100000)], 10):
    #     print(check(i))
