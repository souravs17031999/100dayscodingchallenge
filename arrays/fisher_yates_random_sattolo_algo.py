# program to shuffle the list, generating a random permutation of the list using fisher yates algorithm
# The permutation generated should be uniform meaning every permutation should be equally probable.
# --------------------------------------------------------------------------------------------------------------------------------
# Naive solution will be to loop around the array using index i, and choose second index j again from anywhere in the list
# and swap elements at those indices.
# i => 0....n - 1,
# j => 0.....n - 1
# Suppose our list had 3 elements: [a, b, c]. This means it'll make 3 calls to get_random(0, 2).
# That's 3 random choices, each with 3 possibilities. So our total number of possible sets of choices is 3*3*3=27.
# Each of these 27 sets of choices is equally probable.
# But how many possible outcomes do we have? , know the answer is 3! = 6
# Which is not evenly divisible by 27 hence not euqally probable.
# OR we can also simply take a given arr/list, and keep choosing the random element and pop it from the array, and append the randomly chosen element to the new array.
# The above approaches are in 0(N^2).
# ---------------------------------------------------------------------------------------------------------------------------------
# Better approach ?
# the logic is to simply randomly select a index from i to last element where i will vary from 0 to length of list,
# and swap that with the current element , so all in-place swapping based on random index chosen from remaining list every time.
# i => n - 1 ..... 1,
# j => 0 .... i
# or we do the opposite, we go i from  0 ..... 1,
# and j from i .... n

# The above approaches distribute the probability more uniformly.
# rand() function generates unifrom distribution from 0....1, and get the floor of it to get nearest round integer.
# This random function distributes the number line into euqally probable buckets where the indices may lie.

# explanation of probability below :

# time : 0(N)
# space : 0(1)

# ------------------------------------------------------------------------------------------------------------------
# sattolo's algorithm : if we want to generate permutation with exactly one cycle,
# Logic is to not allow to swap with the current element with itself.
# This will allow for exactly one cycle to exist in the array.
# Array cycles can be visualized as follows :
# EX. Let's say we have following list : [0, 2, 3, 1,]
# 0 -> 0
# 1 -> 2
# 2 -> 3
# 3 -> 1
# If we traverse this graph, we see that there are two cycles. 0 -> 0 -> 0 ... and 1 -> 2 -> 3 -> 1....
# Then, after applying sattolo for first times, let's say,
# Let's say we swap the element in position 0 with some other element. It could be any element,
# but let's say that we swap it with the element in position 2. Then we'll have the list 3 2 0 1, which can be thought of as the following graph:
#
# 0 -> 3
# 1 -> 2
# 2 -> 0
# 3 -> 1
# If we traverse this graph, we see the cycle 0 -> 3 -> 1 -> 2 -> 0.... This is an example of a permutation with exactly one cycle.
# -----------------------------------------------------------------------------------------------------------------------

import random

def shuffle_from_left(arr):

    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [l[0]]
    for i in range(len(arr) - 1, -1, -1):
        random_ele = random.randint(0, i + 1)
        arr[i], arr[random_ele] = arr[random_ele], arr[i]
    return arr

# Earlier the probability of element being landed at index 0 being 1/n and not being placed at index 0 being 1 - (1/n) => (n - 1) / n
# to land up in 1...n - 1, therefore 0 is uniformly placed.
# next element has probability being [1 / (n - 1)] * [(n - 1) / n]
# Inductively, an element lands at position i with probability,
# (n - 1 / n) * (n - 2 / n - 1) * (n - 3 / n - 2)......(n - i/ n - i + 1) * (1/n - i) = 1/n
# so, every element has uniform probability.

def shuffle_from_right(arr):

    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [l[0]]
    for i in range(len(arr) - 1):
        random_ele = random.randint(i, len(arr)-1)
        arr[i], arr[random_ele] = arr[random_ele], arr[i]
    return arr

if __name__ == '__main__':
    l = [20, 4, 9, 0, 1, 11, 5, 30, 2, 15]
    print(shuffle_from_left(l))
    print(shuffle_from_right(l))
