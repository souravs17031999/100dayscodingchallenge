# program to return true if there are two distinct indices such that their difference
# is less than or equal to some given value of k.
# idea is to use a hash map (dict) to store key as element and value as their last seen index ,
# in this way when we see already seen element (key already present in the dict) , then
# we simply check the difference condition to be less than k , and return bool value accordingly
# time : 0(N), space : 0(N)

def closest(arr, k):
    if len(arr):
        count = {}
        flag = False
        for i in range(0, len(arr)):
            if arr[i] in count:
                if abs(i - count[arr[i]]) <= k:
                    flag = True

            count[arr[i]] = i
        return flag
    else:
        return False

if __name__ == '__main__':
    assert closest([0, 1, 2, 3, 5, 2], 3) == True
    assert closest([1,2,3,1], 3) == True
    assert closest([1,0,1,1], 1) == True
    assert closest([1,2,3,1,2,3], 2) == False
    assert closest([], 1) == False
    assert closest([1, 2, 3, 4, 5], 1) == False
    assert closest([1, 2, 2, 4, 5, 2, 5, 8, 4, 2], 5) == True
