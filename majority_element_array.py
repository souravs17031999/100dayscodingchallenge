# Program to find the majority element that is the occurence should be greater than N/2 , where N is the size of the array

# METHOD 4 STARTS
# THIS USES BOYER - MOORE VOTING ALGORITHM
# BEST METHOD , TAKES 0(N) TIME, 0(N) SPACE BUT AGAIN IT ASSUMES MAJORITY ELEMENT EXISTS
# logic is to simply keep an counter of elements when repeated to be seen, and keep a variable for setting majority element, as soon as we see the same
# element , we increase its count, and as soon as we see some another element, we decrease the count till 0, when we change the majority element now to # # be at the current element as a new candidate and start the counter again , finally at the end, we will be having our majority element stored.
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
