# Program for printing top k frequent elements from the given input array
# Naive approach is to keep a count of all numbers in the array in a extra array in a tupled way
# (element, count) and then sort it on the basis of their frequencies and return the elements for
# top k frequencies and this would take atleast 0(N*lg(N)).
# Can we do better than this ?
# So, we can observe since we need count, so we will use collections.Counter for better performance
# and also we can use Counter.most_common() which inbuilt uses heap when given some "k" as input.
# So, overall we are building the array to sort it and return it k times by popping from root.
# So, either we can build a heap and pop it k times or we can use directly above said functions.
# In both case, max bound will be 0(k * (lg(N))) and space : 0(N) for building the heap.
# Can we do more better than this ?

# [0(N) + 0(K) + N*lg(N)] = bounded by N * lg(N) since K < N solution :
from typing import List
from collections import Counter
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    count = count.most_common(k)
    res = []
    for i in range(k):
        res.append(count[i][0])
    return res


if __name__ == '__main__':
    arr, k = [1, 1, 1, 2, 2, 3], 2
    print(topKFrequent(arr, k))
