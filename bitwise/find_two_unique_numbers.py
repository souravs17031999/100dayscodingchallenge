# program to find two unique numbers (non-repeating numbers)
# IDEA: So, first naive approach is to use sorting and check which consecutive ones are non repeating ,
# then comes first efficient solution to use is hashing and store occurences and then traverse through occurence table to find which ones are non repeating.
# Most efficient logic here is to use the bit manipulation XOR trick to efficiently compute the two unique numbers (somehwat same as in one unique number),
# So, what we do is first find that Overall XOR of that number , now this result contains that two numbers combined and we need to extract that one by one,
# firstly, we extarct one of the numbers by finding right most set ("1") bit in the XOR result and then, since it is 1, then only one of them should have "1" # in their binary format , so we traverse through the array and do AND-ing using mask (pos of right most index) we get that particular set of numbers which
# has set bits in their position speicified (we are looking for), and then we keep taking running XOR of this newly found set whenever there is set bit
# detected at that position and in this way first number is extracted, then we simply do XOR of earlier found overall XOR and this number which simply yields # use the second number.
# In a way, we have partitioned the array where one half is containing all those which have set bits in the kth pos as found above, and "x" can be find by either one half.
# So, we consider all those number which have set bits in the same pos, and extract "x" by XORing all of them.
# This solution takes TIME : 0(N) , SPACE: 0(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------
# More better intuition :
# The first step is to do XOR of all elements present in array.
# So we have XOR of x and y after the first step. Let the value of XOR be xor2. Every set bit in xor2 indicates that the corresponding bits in x
# and y have values different from each other. For example, if x = 6 (0110) and y is 15 (1111), then xor2 will be (1001), the two set bits in xor2
# indicate that the corresponding bits in x and y are different. In the second step, we pick a set bit of xor2 and divide array elements in two
# groups. Both x and y will go to different groups. In the following code, the rightmost set bit of xor2 is picked as it is easy to get rightmost
# set bit of a number. If we do XOR of all those elements of array which have the corresponding bit set (or 1),
# then we get the first unique number.
# Let's say, some kth bit is set to 1 in Xor2, then we will partition the overall array such that first group will be having all their kth bits set to 1, other group will not
# So, already other numbers were in pair, they will remain in pair and so, now in one of the group, if we apply XOR of all, then we will get either x or y.
# Now, we can get the other number as overall XOR ^ (x or y) whatever has been found , will give other number.
# -----------------------------------------------------------------------------------------------------------------------------------------------


def two_unique_numbers(arr):
    # find overall XOR
    res = 0
    for i in arr:
        res ^= i

    # trick to find position of right most set bit directly
    pos = res & ~(res - 1)
    # can also be done by simply iterating over the number and right shifting it unless we get first
    # set bit
    # temp = res
    # while temp&1 != 1:
    #     pos += 1
    #     temp = temp >> 1

    # setting x, y initially to 0
    x, y = 0, 0
    # finding which numbers have set bit at this position found , and taking running XOR to find first number
    for i in range(len(arr)):
        if arr[i] & pos:
            x ^= arr[i]

    # at this point, we have found first number,

    # now, simply finding second number
    y = res ^ x

    print(x)
    print(y)

if __name__ == '__main__':
    l = [1400, 2, 4, 2, 4, 199, 5, 5]
    two_unique_numbers(l)
