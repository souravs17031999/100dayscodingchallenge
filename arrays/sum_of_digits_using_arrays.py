# program to calculate sum of digits using input arrays containing digits of numbers
# IDEA: logic is to iterate through last index of both arrays simulataneously calculating sum and also maintaining carry while adding it to previous indices of both arrays.
# so, we need to maintain two variables one for answer of sum and other for carry, here we are using answer(sum) as a list so we can append each digit one by one
# so, first sum of all digits till smaller arrays and then after that only adding carry and remaining digits of remaining array(bigger one)

# function to calculate sum of digits of both arrays after ensuring that first array is always bigger in size than the other one
def sum_array(l1, l2, m, n):
    # setting pointers to both of first arrays
    i = m - 1
    j = n - 1
    carry = 0
    ans = []
    # adding the digits of both arrays till the lower array index exhausts
    while(j >= 0):
        temp = l1[i] + l2[j] + carry
        ans.append(temp%10)
        carry = temp // 10

        j -= 1
        i -= 1

    # adding the remaining digits of bigger array and carry
    while(i >= 0):
        temp = l1[i] + carry
        ans.append(temp%10)
        carry = temp // 10
        i -= 1

    # if there is remaining carry at the last , simply add it to the answer(sum)
    if (carry):
        ans.append(carry)
    return ans[::-1]

# function to make sure to pass bigger array from both of them in the sum_array function
def sum_main(l1, l2, m, n):
    # if length of first array is bigger, then pass this
    if m >= n:
        return sum_array(l1, l2, m, n)
    # otherwise pass second list with its appropriate lengths
    else:
        return sum_array(l2, l1, n, m)

# main function
if __name__ == '__main__':
    m = int(input().strip())
    l1 = list(map(int, input().strip().split()))
    n = int(input().strip())
    l2 = list(map(int, input().strip().split()))
    s = sum_main(l1, l2, m, n)
    for i in range(len(s)):
        s[i] = str(s[i])
    print(' '.join(s))

'''
assert sum_main([1, 2, 3, 4, 5, 6], [6, 7, 8, 9], 6, 4) == [1, 3, 0, 2, 4, 5]
'''
