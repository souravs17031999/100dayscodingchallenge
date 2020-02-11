# program to find odd occured element , if there is only one odd occurence element
# one of the optimized approach would be to create hashmap and store all the occurences of every char, and then traversing over it and
# check if it is odd, then print corresponding element
# Best optimized approach is to use XOR bitmasking, as same elements would vanish , as in case of even occurence, whereas
# different elements would appear as in odd , final result would get us that particular element which has odd occurence.
# method 1
# time complexity : 0(N)
# space complexity : 0(N)
# def find_occ(arr):
#     arr_size = len(arr)
#     max_value = max(arr) + 1
#     count = [0]*max_value
#     for i in range(arr_size):
#         count[arr[i]] += 1
#     for i in range(len(count)):
#         if count[i] & 1:
#             return i
# method 2
# time complexity : 0(N)
# space complexity : 0(1)
def find_occ(arr):
    res = 0
    for i in range(len(arr)):
        res = res ^ arr[i]
    return res

if __name__ == '__main__':
    assert find_occ([1, 2, 3, 2, 3, 1, 3]) == 3
    assert find_occ([5, 7, 2, 7, 5, 2, 5]) == 5
