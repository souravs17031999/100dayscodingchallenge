# function to convert decimal number to binary
# IDEA: logic is that first, we can get last bit by simply ANDing with 1 , and keep right shifting by 1 , but then we will get reverse of the number
# so, we need to actually move from end towards start and keep combining running sum in the form of base10 calculation by multiplying every digit extracted by
# correspoding power of 10 and adding it to the running sum obtained so far.

def decimal_to_binary(x):
    ans = 0
    power = 1
    while (x > 0):
        ans += (x & 1) * power
        x = x >> 1
        power *= 10
    return ans

print(decimal_to_binary(3))
