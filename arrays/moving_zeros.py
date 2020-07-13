# program for moving all zeroes to the end and all
# non zero elements at the front with the same relative ordering.
# Optimized approach : 
# Idea here is to take a counter, and then simply for every non-zero element, we can increment counter and place the element at that index of the array, in this way, all non-zero
# elements will be at the front maintaining their relative order, then simply put zeroes for the remaining lenght of the array.
# TIME : 0(N), SPACE : 0(1).

def moveZeroes(nums) -> None:
        n = len(nums)
        ptr = 0
        for i in range(0, n):
            if nums[i] != 0:
                nums[ptr] = nums[i]
                ptr += 1

        for i in range(ptr, n):
            nums[i] = 0
