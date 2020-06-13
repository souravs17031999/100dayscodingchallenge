# Program to compute prefix sum or cummulative sum array so that at every point, we have value equal to sum of all number from 0 to till that index.
# TIME : 0(N), SPACE : 0(N), WHERE N IS SIZE OF INPUT ARRAY 

def prefix_sum(arr):
    if not len(arr):
        return []
    cum_sum = [0 for _ in range(len(arr))]
    cum_sum[0] = arr[0]
    for i in range(1, len(arr)):
        cum_sum[i] = cum_sum[i - 1] + arr[i]

    return cum_sum

if __name__ == '__main__':
    arr =[10, 4, 16, 20]
    print(prefix_sum(arr))
