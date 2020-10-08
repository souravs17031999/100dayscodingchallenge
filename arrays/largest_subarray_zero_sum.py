# Program for computing largest length of subarray with zero sum.
# Naive solution will be to have two outer loops, and then sum it up from first idx to second idx, 
# in 0(N^3).
# Then, we can slightly optimize and keep running sum while inside inner loops, in 0(N^2).
#
# arr : [15, -2, 2, -8, 1, 7, 10, 23]
#
# 15
# 15, -2
# 15, -2, 2
# 15, -2, 2, -8
# 15, -2, 2, -8, 1
# .....
# -2
# -2, 2
# -2, 2, -8
# -2, 2, -8, 1
# -2, 2, -8, 1, 7 => {0}
#
# Can we do better than this ?
# ---------------------------------------------------------------------------------------------------------
# We can keep a HashMap and put in the key:value pair, {prefix-sum : index of first occ.}
# Now, index of first occ. is very important and when traversing the array, if we see the sum value 
# already in the hashmap, then it means that the next part of original subarray is 0 like shown below.
#
# -------------------    
# 15, -2, 2, -8, 1, 7, 10, 23
# __                             => S : 15 and it is already in hashmap : {15:0}
#                   ^ 
#                   |
# 
# Now, S : 15, again at idx : 5 - 0 => 5
#
# [15, -2, 2, -8, 1, 7, 10, 23]

# {15:0, 13:1, 7:3, 8:4, 25:6}

# max : 5
# TIME : 0(N), SPACE : 0(1)
# ---------------------------------------------------------------------------------------------------------

def compute_largest_sum(arr):
    
    n = len(arr)
    map = {}
    sum = 0
    max_sum = 0
    for i in range(n):
        sum += arr[i]
        
        if arr[i] == 0 and max_sum == 0:
            max_sum = 1
        
        if sum == 0:
            max_sum = i + 1
            
        if sum not in map:
            map[sum] = i 
        else:
            max_sum = max(max_sum, i - map[sum])
    
    return max_sum

if __name__ == '__main__':
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    print(compute_largest_sum(arr))
