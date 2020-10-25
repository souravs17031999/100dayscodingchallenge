# Program to find first occurence of least greater value than key given in the array and similarly last occurence of greater value than key.
# Intution is modified binary search , also a follow up from previous problem.
# -----------------------------------------------------------------------------------------------------
# TIME : 0(log(N)), space : 0(1)

# just greater than key , so it will be first least 
def first_least_greater(arr, key):
    
    pos = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        
        if key < arr[mid]:
            pos = mid
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            start = mid + 1
    
    return pos

# just less than key, so it will be last greater 
def last_greatest_lesser(arr, key):
    
    pos = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            pos = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return pos
    
arr = [2, 3, 3, 5, 5, 5, 6, 6]
print(first_least_greater(arr, 5))
print(last_greatest_lesser(arr, 5))
