# arr = [2, 0, 1, 0]
# # ptr -> pointing to the first index, as
# # i = 0 => hop 2 position => ptr at i = 1, then hop 1 position , ptr = > at i = 3 so, correct !
# # i = 1 => hop 0 position ...
# # i = 1 => hop 1 position => ptr at i = 3, so correct !
# #
# # so, for every i, we are using ptr to hop to forward and check if it reaches the end !
# #
# # this takes 0(N^2) in worst case
# can we do better ?



def canReachEnd(arr):
    n = len(arr)
    for i in range(n):
        ptr = i
        print(f"outer ptr : {ptr}")
        while ptr < n and arr[ptr] != 0:
            print(f"inner ptr : {ptr}")
            if ptr == n - 1:
                return 1
            if arr[ptr] == 0:
                return 0    
            ptr = ptr + arr[ptr]
            print("inner finished ")


if __name__ == '__main__':
    arr = [3, 2, 1, 0, 4]
    print(canReachEnd(arr))
