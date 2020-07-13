# program to return first and last occurence of element x in sorted array
# logic is to use the information for stored array and use modified binary search algorithm.
# Idea is to whenever we find the required element, then we should not stop ,
# but rather go on in left for finding first occurence or go on in right
# for finding last occurence.
# We can construct two separate functions for acheiving this two positions by changing just at the time when arr[mid] == x, 
# so that we don;t stop there and keep exploring from there either in left space or in right space depending upon which occcurence is needed.
# We can also combine both the condition in one line as finding greater than or
# equal to x, and then for x + 1 (now this will be start of some other element)
# greater than x but the position will indicate the last occurence of x
# TIME 0(lg(n)), SPACE : 0(1)

# the function for returning required index
def first_and_last(arr, x):
    # we set this as array size, (max) as in the case of all the elements being
    # same in the array, this should return the length of array (last index)
    low, high = 0, len(arr) - 1
    index = len(arr)
    # modified bin search
    while low <= high:
        mid = low + (high - low) // 2
        # we keep on looking
        if arr[mid] >= x:
            index = mid
            high = mid - 1
        else:
            low = mid + 1
    return index

# main driver function
if __name__ == '__main__':
    arr = [1, 1, 1, 1] # this is the case which is why need to set index = len(arr)
    x = 1
    n = 2
    first_pos = first_and_last(arr, x)
    print(first_pos)
    last_pos = first_and_last(arr, x + 1) - 1
    print(last_pos)
    # now if we do not find any occurence, then last pos will be lesser than
    # first , then we need to return [-1, -1], ex. searching for 9 in above array
    # returns 4, 3 which fails for below if condition and so [-1, -1]
    if first_pos <= last_pos:
        print([first_pos, last_pos])
    else:
        print([-1, -1])
