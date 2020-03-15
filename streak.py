# program to return the maximum streak in a array containing tosses results of some rounds as [heads, heads, tails, ......]

def maximum_stream(arr):
    max_count_h, max_count_t = 0, 0
    curr_count_h, curr_count_t = 0, 0
    for i in range(0, len(arr)):
        if arr[i] == 'H':
            curr_count_h += 1
            curr_count_t = 0
            max_count_h = max(max_count_h, curr_count_h)
        else:
            curr_count_t += 1
            curr_count_h = 0
            max_count_t = max(max_count_t, curr_count_t)
    return [max_count_h, max_count_t]

if __name__ == '__main__':
    assert maximum_stream(['H', 'T', 'T', 'T', 'H', 'H', 'T']) == [2, 3]
    assert maximum_stream(['H', 'H', 'H', 'T', 'T', 'H', 'H', 'H', 'H', 'T']) == [4, 2]
    assert maximum_stream(['H']) == [1, 0]
    assert maximum_stream(['T', 'T', 'T']) == [0, 3]
    assert maximum_stream(['H', 'H', 'H', 'H']) == [4, 0]
