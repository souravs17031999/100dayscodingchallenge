# Program for getting the minimum cost of joining the given n number of ropes efficiently.
# Cost is defined by the lengths of the ropes given to us as input.
# We can observe, that if we follow greedy approach such that we always choose next minimum element to
# be added to the already made rope so far, this would lead to overall minimum cost.
# For tracking current minimum and next minimum element, a binary heap is optimized version of maintaining this.
# So, everytime we extract two minimum from the min heap and then add them to the cost so far, and then push back the the
# popped element cost again in the heap as we also want to keep track of old cost to be added in the next iteration.
# This goes on till we have atleast two elements in the heap.
# TIME : 0(lg(N))


from heapq import heappush, heappop, heapify

def MinJoin(arr):
    heapify(arr)
    cost = 0
    while len(arr) > 1:
        a, b = heappop(arr), heappop(arr)
        cost += (a + b)
        heappush(arr, a + b)

    return cost


if __name__ == '__main__':
    arr = [4, 3, 2, 6]
    print(MinJoin(arr))
