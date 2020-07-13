# function to calculate sum of digits of both arrays after ensuring that first array is always bigger in size than the other one
# Idea is similar to the array digit sum, just a variation will be in getting exact number from the string without int() conversion,
# and that will be done by using ASCII values using ord() , ord('i') - ord('0') will get us the number i.

def sum_array(s1, s2, m, n):
    i = m - 1
    j = n - 1
    carry = 0
    ans = ""
    # adding the digits of both arrays till the lower array index exhausts
    while(j >= 0):
        temp = (ord(s1[i]) - ord('0')) + (ord(s2[j]) - ord('0')) + carry
        ans = f"{ans}{temp%10}"
        carry = temp // 10

        j -= 1
        i -= 1

    # adding the remaining digits of bigger array and carry
    while(i >= 0):
        temp = (ord(s1[i]) - ord('0')) + carry
        ans = f"{ans}{temp%10}"
        carry = temp // 10
        i -= 1

    # if there is remaining carry at the last , simply add it to the answer(sum)
    if (carry):
        ans = f"{ans}{carry}"

    return ans[::-1]

if __name__ == '__main__':
    s1 = '3333311111111111'
    s2 = '44422222221111'
    m, n = len(s1), len(s2)
    if m > n:
        print(sum_array(s1, s2, m, n))
    else:
        print(sum_array(s2, s1, n, m))
