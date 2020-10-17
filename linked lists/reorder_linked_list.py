"""
Problem :
Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You must do this in-place without altering the nodes’ values.
For example, Given {1,2,3,4}, reorder it to {1,4,2,3}.

Approach :)
We can divide this problem into two simple problems of 
1) Length of SLL(Singly Linked List) 
2) Reversing a SLL and Merging two SLL’s alternatively. 

We first get the length of the SLL and divide it to two parts. 
We reverse the second part of our SLL and apply the process of 
merging the first SLL and reversed second SLL alternatively will give us the required result.
"""
from math import ceil
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        #if we have zero or one node in SLL then return
        if(head is None or head.next is None):
            return
        #Get the length of the SLL
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        temp = head
        for i in range(ceil(length/2) - 1):
            temp = temp.next
        prev = temp
        temp = temp.next
        #Breaking the SLL into two parts
        prev.next = None

        #Reversing the second part of SLL
        prev = None 
        curr = temp
        while curr:
            nextEle = curr.next
            curr.next = prev
            prev = curr
            curr = nextEle
        #Merging the first half of SLL
        #and Reversed second half of SLL
        #Alternatively
        firstList = head
        secondList = prev
        while(firstList and secondList):
            firstNext = firstList.next
            secondNext = secondList.next
            firstList.next = secondList
            secondList.next = firstNext
            firstList = firstNext
            secondList = secondNext
        #Printing the Result
        while head:
            print(head.val)
            head = head.next
chain = ListNode(1)
chain.next = ListNode(2)
chain.next.next = ListNode(3)
chain.next.next.next = ListNode(4)
chain.next.next.next.next = ListNode(5)
sol = Solution()
sol.reorderList(chain)
