# Program for creating custom data structure for efficient following operations based on frequency :
#-------------------------------------
# findMin() : Returns the minimum item. Frequency: Most frequent
# findMax() : Returns the maximum item. Frequency: Most frequent
# deleteMin() : Delete the minimum item. Frequency: Moderate frequent
# deleteMax() : Delete the maximum item. Frequency: Moderate frequent
# Insert() : Inserts an item. Frequency: Least frequent
# Delete() : Deletes an item. Frequency: Least frequent.
#-------------------------------------
# Optimized approach :
# We can observe that Most frequent operations are findMax and findMin, so we need to build and maintain two binary heaps -
# minheap and maxheap to get those in 0(1).
# Now, deleteMax and deleteMin , this is also done in lg(n) time.
# Insert() and Delete() are less frequent and hence can be made costly (tradeoffs !) - 0(N).
# Now, to make sure we are properly inserting and delete, how do we manage both the heaps at the same time as we do not know already
# what order does the data maintains as the data can be random , so we need to maintain max and min both at the same time.
# For linking both heaps, we need some extra temp data structures, here "Doubly linked list", which will basically contain
# the values which we insert and along with it the indices of minheap and maxheap where it stores the elements so that we maintain
# min and max both at the same time , and also while deleting, we need to delete from all the three data structures.

import sys
import random
# structure for node class
class Node:

    def __init__(self, x):
        self.data = x
        self.minIdx = None
        self.maxIdx = None
        self.prev = None
        self.next = None

# class structure for doubly_linked_lists
class doubly_linked_lists:

    def __init__(self):
        self.head = None

    # function for inserting the element at the end of doubly_linked_lists
    def push(self, node, minIdx, maxIdx):

        if not self.head:
            self.head = node
            node.minIdx = minIdx
            node.maxIdx = maxIdx
            return

        self.head.prev = node
        node.next = self.head
        self.head = node
        node.minIdx = minIdx
        node.maxIdx = maxIdx

    # function for removing node given any address
    def remove_node(self, node):

        if not self.head:
            raise Exception ("Linked lists empty !")

        if self.head.next == None:
            self.head = None
            del node
            return

        if not node.prev:
            self.head = node.next
            node.next.prev = None
            node.next = None
            return

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        del node
        node = None
        return

    # function for deleting node given any values
    def delete_node(self, x):

        if not self.head:
            raise Exception ("Linked lists empty !")

        ptr = self.head
        while ptr and ptr.data != x:
            ptr = ptr.next

        if not ptr:
            raise Exception ("Element not found in the DS!")

        minIdx, maxIdx = ptr.minIdx, ptr.maxIdx
        self.remove_node(ptr)
        return minIdx, maxIdx

    # printing the traversal of doubly_linked_lists
    def pretty_print(self):

        if not self.head:
            raise Exception ("Linked lists empty !")

        ptr = self.head
        while ptr != None:
            print(ptr.data, end = "->")
            ptr = ptr.next

# class structure for MinHeap
class MinHeap:

    def __init__(self, maxsize = 1000):
        '''
        maxsize : maxsize is default 1000, otherwise we can set it.
        '''
        self.maxsize = maxsize
        # we initialize a list of maxsize elements to avoid extending lists every time.
        self.heap = [[None, None] for _ in range(maxsize)]
        # it keeps a track of current size of actual heap.
        self.size = 0

    # helper function for getting parent of any node at index i
    def parent(self, i):
        return i // 2

    # helper function for getting left child of any node at index i
    def left(self, i):
        return 2 * i + 1

    # helper function for getting right child of any node at index i
    def right(self, i):
        return 2 * i + 2

    # function for pushing the element onto heap
    def heappush(self, node):
        self.size += 1
        if self.size > self.maxsize:
            raise Exception ("Heap Overflow reached !")

        # print(f"current heap size : {self.size}")
        self.heap[self.size - 1][0] = node.data
        self.heap[self.size - 1][1] = node
        idx = self.size - 1
        while idx > 0 and self.heap[self.parent(idx)][0] > self.heap[idx][0]:
            self.heap[self.parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.parent(idx)]
            idx = self.parent(idx)

        return idx

    # function for heapfiying
    def MinHeapify(self, i):
        # we initialize the largest to be current element (element to be swapped)
        smallest = i
        left = 2 * i + 1  # extract left index
        right = 2 * i + 2 # extract right index

        # we compare the left child with the current element and set it largest if its maximum that current element
        if left < self.size and self.heap[left][0] < self.heap[i][0]:
            smallest = left

        # now, since we are comparing the current maximum so far with the right child, hence we obtain overall maximum
        if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        # if there is a change in largest, it means there is voilation of heap property and we need to swap
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            # call heapify recursively for every node one by one top to down
            self.MinHeapify(smallest)


    # function for popping from the heap
    def heappop(self):
        if self.size:
            pop_value = self.heap[0]
            self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
            # del self.heap[self.size - 1]
            self.size -= 1
            self.MinHeapify(0)
            return pop_value
        else:
            raise Exception ("Heap is already empty !")

    # function to get minimum from the heap
    def getMin(self):
        if self.size:
            return self.heap[0][0]
        else:
            raise Exception ("Index doesn't exist !")
            

    # printing the heap
    def printheap(self):
        if self.size:
            for i in range(self.size):
                print(self.heap[i], end = " ")
            print()
        else:
            raise Exception ("Empty heap !")


# class structure for MaxHeap
class MaxHeap:

    def __init__(self, maxsize = 1000):
        '''
        maxsize : maxsize is default 1000, otherwise we can set it.
        '''
        self.maxsize = maxsize
        # we initialize a list of maxsize elements to avoid extending lists every time.
        self.heap = [[None, None] for _ in range(maxsize)]
        # it keeps a track of current size of actual heap.
        self.size = 0

    # helper function for getting parent of any node at index i
    def parent(self, i):
        return i // 2

    # helper function for getting left child of any node at index i
    def left(self, i):
        return 2 * i + 1

    # helper function for getting right child of any node at index i
    def right(self, i):
        return 2 * i + 2

    # function for pushing the element onto heap
    def heappush(self, node):
        self.size += 1
        if self.size > self.maxsize:
            raise Exception ("Heap Overflow reached !")

        # print(f"current heap size : {self.size}")
        self.heap[self.size - 1][0] = node.data
        self.heap[self.size - 1][1] = node
        idx = self.size - 1
        while idx > 0 and self.heap[self.parent(idx)][0] < self.heap[idx][0]:
            self.heap[self.parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.parent(idx)]
            idx = self.parent(idx)

        return idx

    # function for heapfiying
    def MaxHeapify(self, i):
        # we initialize the largest to be current element (element to be swapped)
        largest = i
        left = 2 * i + 1  # extract left index
        right = 2 * i + 2 # extract right index

        # we compare the left child with the current element and set it largest if its maximum that current element
        if left < self.size and self.heap[left][0] > self.heap[i][0]:
            largest = left

        # now, since we are comparing the current maximum so far with the right child, hence we obtain overall maximum
        if right < self.size and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        # if there is a change in largest, it means there is voilation of heap property and we need to swap
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            # call heapify recursively for every node one by one top to down
            self.MaxHeapify(largest)

    # function for popping from the heap
    def heappop(self):
        if self.size:
            pop_value = self.heap[0]
            self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
            # del self.heap[self.size - 1]
            self.size -= 1
            self.MaxHeapify(0)
            return pop_value
        else:
            raise Exception ("Heap is already empty !")

    # function to get minimum from the heap
    def getMax(self):
        if self.size:
            return self.heap[0][0]
        else:
            raise Exception ("Index doesn't exist !")

    # printing the heap
    def printheap(self):
        if self.size:
            for i in range(self.size):
                print(self.heap[i], end = " ")
            print()
        else:
            raise Exception ("Empty heap !")


class EfficientHeap:

    def __init__(self):
        self.dlist = doubly_linked_lists()
        self.MinHeap = MinHeap()
        self.MaxHeap = MaxHeap()

    def insert(self, x):
        new_node = Node(x)
        minIdx = self.MinHeap.heappush(new_node)
        maxIdx = self.MaxHeap.heappush(new_node)
        self.dlist.push(new_node, minIdx, maxIdx)

    def delete(self, x):
        minIdx, maxIdx = self.dlist.delete_node(x)



    def getMin(self):
        return self.MinHeap.getMin()

    def getMax(self):
        return self.MaxHeap.getMax()

    def deleteMin(self):
        value, address = self.MinHeap.heappop()
        self.dlist.remove_node(address)
        return value

    def deleteMax(self):
        value, address = self.MaxHeap.heappop()
        self.dlist.remove_node(address)
        return value

    def pretty_print(self):
        self.dlist.pretty_print()


if __name__ == '__main__':
    DS = EfficientHeap()
    l = [random.randint(0, 1000) for _ in range(10)]
    print(f"Elements selected : {l}")
    for i in l:
        DS.insert(i)
    print(f"Minimum :  {DS.getMin()}")
    print(f"Maximum :  {DS.getMax()}")
    print(f"Maxdelete :  {DS.deleteMax()}")
    print(f"Mindelete :  {DS.deleteMin()}")
    print(DS.pretty_print())
