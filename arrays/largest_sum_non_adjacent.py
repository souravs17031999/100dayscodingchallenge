# # find the largest possible sum for non adjacent numbers
# Thniking in rough ----------------------------------------------------------
# EX. arr = [2, 4, 6, 2, 5] ,
# start from 2 , and then we check for non adjacent pairs possible  :
# 2 6 5
# 2 2
# 2 5
# 4 2
# 4 5
# 6 5
# 2
#
# => 13 (2, 6, 5)
#
# Ex. arr = [5, 1, 1, 5]
# start from 5 and then we check......
# 5 1
# 5 5
# 1 5
# 1
#
# => 10 (5, 5)
# #-------------------
#
# arr = [5, 5, 10, 40, 50, 35]
#
# incl = 5
# excl = 0
#
# for i = 1: incl = 5, excl = max(5, 0) = 5
# for i = 2 : incl = 15, excl = max(5, 5) = 5
# for i = 3 : incl = 45, excl = max(5, 15) = 15
# Naive approach would be 0(N^3).
# OPTIMIZED approach :
# NOW, we can think that at any element, either we can take that element or
# we don't take that element.
# we loop around and for every element, we maintain two variables : incl, excl =>
# incl inluding max sum including previous element
# excl including max sum excluding previous element
# so, let's say at any point, we don't take that element, so we can take previous element, also
# excl will be affected, so excl = max(incl, excl)
# Now, let's say we take that element, and so we can't take the previous element now,
# hence, incl will be affected, then, incl = excl + arr[i]
# TIME : 0(N), SPACE : 0(1), WHERE N IS LENGTH OF ARRAY.

def compute_max(arr, n):
    incl = arr[0]
    excl = 0
    for i in range(1, n):
        # we keep a temporary var temp_excl so that in next iteration, we require last value of
        # excl to be inluced in excl formula
        temp_excl = max(incl, excl)
        incl = excl + arr[i]
        excl = temp_excl

    return max(incl, excl)

if __name__ == '__main__':
    arr, n = [5, 5, 10, 100, 10, 5], 6
    print(compute_max(arr, n))
