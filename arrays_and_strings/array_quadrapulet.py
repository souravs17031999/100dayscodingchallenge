# Program to first find all the quadraples, which sum up to some specific target sum, and then extend this by including only the unique quadraples.

# below program is complete in the sense that it is already extended for only unique quadraples
# logic is to set two pointers fixed for every iteration of two loops , and then use one more inner loop for solving two pair sum problem where the
# target will be the remaining sum after subtraction the other numbers from the Original target.
# This technique uses two pointer approach and extends it for four pointers
# TIME : 0(n^3) , space : 0(1)
def find_array_quadra(arr, s):
    # getting the size of array
    n = len(arr)
    # it is not possible to get a quadraples from array of less than 4 size
    if n == 0 or n < 4:
        return []
    # first we sort the array so that we can apply two pointer approach
    arr.sort()
    # empty list used to store all answers and return
    result = []
    # fixing one pointer (first number)
    for i in range(0, n - 3):
        # check for duplicate element , if true then skip this iteration
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        # fixing another pointer (second number)
        for j in range(i + 1, n - 2):
            # check for duplicate element , if true then skip this iteration
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            # computing remaining sum
            remain_sum = s - (arr[i] + arr[j])
            # fixing third and fourth pointers
            start = j + 1
            end = n - 1
            # applying two pointer approach
            while(start < end):
                if arr[start] + arr[end] == remain_sum:
                    result.append([arr[i], arr[j], arr[start], arr[end]])
                    start += 1
                    end -= 1
                    # below both loops are just for skipping duplicates pairs
                    # ex. [1, 2, 3, 4, ...., 6, 6, 6, 6,.... 7, 7, 7], here if we fix two pointers, before repetition of 6 starts, then when we
                    # try to find other two, then we will get same pairs , so we are just skipping those after getting first of them.
                    while start < end and arr[start] == arr[start - 1]:
                        start += 1
                    while start < end and arr[end] == arr[end + 1]:
                        end -= 1

                elif arr[start] + arr[end] < remain_sum:
                    start += 1
                else:
                    end -= 1
    return result
if __name__ == '__main__':
    assert find_array_quadra([2, 7, 4, 0, 9, 5, 1, 3],  20) == [[0, 4, 7, 9], [1, 3, 7, 9], [2, 4, 5, 9]]
    assert find_array_quadra([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2,  0, 0, 2], [-1,  0, 0, 1]]
    assert find_array_quadra([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
    assert find_array_quadra([-3,-2,-1,0,0,1,2,3], 0) == [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
