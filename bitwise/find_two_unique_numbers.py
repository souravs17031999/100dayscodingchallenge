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
