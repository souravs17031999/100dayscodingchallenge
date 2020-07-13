# Program for finding all unqiue pairs for which sums up to some target value in a array

# The idea is to understand the fact that after sorting the whole array, we can observe that if we keep two pointers one at leftmost index and other at rightmost index then, if the sum of both is greater than target, then we know that decrease our pointers otherwise increase it.
def array_target_sum_main(l, target):
    start = 0   # leftmost starting index
    end = len(l) - 1  # rightmost ending index
    l.sort()  # sorting the index
    while(start < end):
        if(l[start] + l[end] == target):    # checking if we got the target
            print(f"{l[start]} {l[end]}")
        # we don't have to stop once we found the sum and try to continue checking if possibility
        if(l[start] + l[end] > target):   # we need to decrease the right pointer because list is already sorted , so we need to decrease the sum
            end -= 1
        else:
            start += 1


n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
target = int(input())
array_target_sum_main(l, target)
