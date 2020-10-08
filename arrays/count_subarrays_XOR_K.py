# Program for counting the subarrays with given XOR value as K.
# Naive solution in 0(N^3)/0(N^2)
# 
# [4, 2, 2, 6, 4]
#
# 4, 
# 4, 2, 
# 4, 2, 2, 
# 4, 2, 2, 6, 
# 4, 2, 2, 6, 4, 
#
# 2, 
# 2, 2, 
# 2, 2, 6, 
# 2, 2, 6, 4, 
# .....
#
# TIME :  0(N^2), SPACE : 0(1)
#
# --------------------------------------------------------------------------------------------------------
#    Xr(i)
# --------
# [4, 2, 2, 6, 4]
#  ____
#   (y)  m=XOR given
#
# Xr(i) => prefix XOR till {i}
# there will be many y's for which we will get m as XOR of remaining array for XOR{i} subarray.
# so, we have to count those y's.
# TIME : 0(N), SPACE : 0(N)
# -------------------------------------------------------------------------------------------------------

def compute_largest_XOR(arr, m):
    
    n = len(arr)
    XOR = [0] * n
    count = 0
    map = {}
    
    for i in range(1, n):
        XOR[i] = XOR[i - 1] ^ arr[i] 
    
    for i in range(n):
        Y = m ^ XOR[i]
        
        if Y in map:
            count += map[Y]
        
        if XOR[i] == m:
            count += 1
        
        map[XOR[i]] = map.get(XOR[i], 0) + 1
    
    print(count)
        
        
if __name__ == '__main__':
    arr = [4, 2, 2, 6, 4]
    compute_largest_XOR(arr, 6)
