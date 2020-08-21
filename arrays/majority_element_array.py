# Program to find the majority element that is the occurence should be greater than N/2 , where N is the size of the array
# BELOW PROGRAMS IN VARIOUS SECTIONS ARE FOR N/2, N/3.... MAJORITY ELEMENTS.
# ----------------------------------------------------------------------------------------------------------------
# NOTE :
# There can be at most one majority element which is more than ⌊n/2⌋ times.
# There can be at most two majority elements which are more than ⌊n/3⌋ times.
# There can be at most three majority elements which are more than ⌊n/4⌋ times.
# -----------------------------------------------------------------------------------------------------------------
# MOST OPTIMIZED METHOD :
# THIS USES BOYER - MOORE VOTING ALGORITHM
# BEST METHOD , TAKES 0(N) TIME, 0(1) SPACE BUT AGAIN IT ASSUMES MAJORITY ELEMENT EXISTS
# logic is to simply keep an counter of elements when repeated to be seen, and keep a variable for setting majority element, as soon as we see the same
# element , we increase its count, and as soon as we see some another element, we decrease the count till 0, when we change the majority element now to # # be at the current element as a new candidate and start the counter again , finally at the end, we will be having our majority element stored.
# -------------------------------------------------------------------------------------------------------------------
# NOTE : One important thing is that BOYER - MOORE VOTING ALGORITHM doesn't tell if the majority element exists, it gives the answer only
# if the majority element exists.
# So, we need to do a second linear time pass to count and check just for the candidates and their count if greater than required N//2, N//3..
# This will allow us to get exactly how many majority elements are present or there are none of them existent.
# --------------------------------------------------------------------------------------------------------------------

def find_majority(arr):
    array_size = len(arr)
    count = 0
    M_element = None
    for i in range(array_size):
        if count == 0:
            M_element = arr[i]
        if arr[i] == M_element:
            count += 1
        else:
            count -= 1
    return M_element

# Majority element occuring |N/3| times :
# --------------------------------------------------------------------------------------------------------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        array_size = len(nums)
        count1, count2, M_element1, M_element2 = 0, 0, None, None
        for i in range(array_size):
            if nums[i] == M_element1:
                count1 += 1
            elif nums[i] == M_element2:
                count2 += 1
            elif count1 == 0:
                M_element1 = nums[i]
                count1 += 1
            elif count2 == 0:
                M_element2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        for i in [M_element1, M_element2]:
            if nums.count(i) > len(nums) // 3:
                result.append(i)
        return result

# ---------------------------------------------------------------------------------------------------------------------
# ALTERNATE METHODS FOR N/2 BUT ARE APPLICABLE FOR OTHERS ALSO WITH SLIGHT MODIFICATIONS..... (FOR SHOWING DIFFERENT METHODS PURPOSES)
# METHOD 3 STARTS
# sorting the array , then middle element will always be the majority element
# time : 0(nlgn), space : 0(1)
# def find_majority(arr):
#     arr.sort()
#     array_size = len(arr)
#     return arr[array_size // 2]
# ------------------*-------------
# METHOD 2 STARTS
# TIME : 0(nlgn), SPACE : 0(1)
# def find_majority(arr):
#     array_size = len(arr)
#     counter = 0
#     if len(arr) == 1:
#         return arr[0]
#     arr.sort()
#     for i in range(1, array_size):
#         if arr[i] != arr[i - 1]:
#             counter = 1
#         else:
#             if i == 1:
#                 counter = 2
#             else:
#                 counter += 1
#             if counter > (array_size) / 2:
#                 return arr[i]
#     return -1
# ------------*----------------------
# METHOD 1 STARTS
# TIME : 0(N), SPACE : 0(N)
# def find_majority(arr):
#     count = {}
#     array_size = len(arr)
#     if len(arr) == 0:
#         return -1
#     for i in range(array_size):
#         if arr[i] in count:
#             count[arr[i]] += 1
#         else:
#             count[arr[i]] = 1
#     for i, j in count.items():
#         if j > (array_size) / 2:
#             return i
#     return -1

if __name__ == '__main__':
    assert find_majority([3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 1, 3, 3]) == 3
    #assert find_majority([1, 2, 3]) == -1
    assert find_majority([3,2,3]) == 3
    #assert find_majority([]) == -1
    assert find_majority([2,2,1,1,1,2,2]) == 2
    assert find_majority([1, 1, 1, 1, 1]) == 1
    #assert find_majority([1,1,1,1,3,3,3,4,4,4]) == -1
    assert find_majority([1]) == 1
    assert find_majority([1, 1]) == 1
