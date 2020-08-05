# The problem statement says that we have to basically maximize the profit collected in the knapsack of
# weight of atmost W, given some array containing items weights and its values.
# Array : {{60, 10}, {100, 20}, {120, 30}}
# (value, weight) pairs.
# -----------------------------------------------------------------------------
# Actually, we can't be able to actually get any kind of greedy approach based on just weights, values
# so, we can get the ratio: value/weight for the items and considering constraints, we can get the items in the knapsack,
# and if at any point , we can't pack more items, then we can simply compute fraction of items and get the remaining
# knapsack filled till W.
# -----------------------------------------------------------------------------
# TIME : 0(N*log(N))

def compute_knapsack(arr, n, W):

    arr.sort(key=lambda x : x[0]/x[1], reverse=True)
    curr_w = 0
    result = 0
    for i in range(n):

        if curr_w + arr[i][1] <= W:
            curr_w += arr[i][1]
            result += arr[i][0]

        else:
            remain = W - curr_w
            result += arr[i][0] * (remain / arr[i][1])
            break

    print(result)

if __name__ == '__main__':

    arr = [[60, 10], [100, 20], [120, 30]]
    compute_knapsack(arr, 3, 50)
