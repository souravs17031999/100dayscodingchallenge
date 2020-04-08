# program for moving all zeroes to the end and all
# non zero elements at the front with the same relative ordering.

def moveZeroes(nums) -> None:
        n = len(nums)
        ptr = 0
        for i in range(0, n):
            if nums[i] != 0:
                nums[ptr] = nums[i]
                ptr += 1

        for i in range(ptr, n):
            nums[i] = 0
