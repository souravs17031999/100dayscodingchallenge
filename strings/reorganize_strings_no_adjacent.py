# Program for reorganizing strings (if possible), such that no two adjacent chars
# are same.
# ---------------------------------------------------------------------------------
# Ex. "aab" => "aba"
# Ex. "aaab" => "aba", and now "a" is remaining, and hence, we can't
# be able to reorganize.
# ---------------------------------------------------------------------------------
# We can observe that greedy approach would work great for this so that every time
# we can get most freq. occuring element so that every time we get diff. element
# and if there is any char left after all the string has been processed,
# then it is not possible for us to reorganize string.
# ---------------------------------------------------------------------------------
# Yeah, we can use Priority Queues for this purpose.
# ---------------------------------------------------------------------------------
from collections import Counter
from heapq import heapify, heappush, heappop

def reorganize_string(s):
    count = Counter(s)
    heap = [(-count.get(i), i) for i in count]
    heapify(heap)
    result = ""
    while len(heap) > 1:
        curr, next = heappop(heap)[1], heappop(heap)[1]
        result = f"{result}{curr}{next}"
        count[curr] -= 1
        count[next] -= 1
        if count[curr]:
            heappush(heap, (-count.get(curr), curr))
        if count[next]:
            heappush(heap, (-count.get(next), next))

    if heap:
        last = heappop(heap)[1]
        if count[last] > 1:
            return ""
        result = f"{result}{last}"

    return result



if __name__ == '__main__':

    reorganize_string("aab") == "aba"
    reorganize_string("aaab") == ""
