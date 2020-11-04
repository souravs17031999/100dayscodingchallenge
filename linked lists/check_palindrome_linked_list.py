# Program to check if the given linked list is palindrome or not.
# NOTE : Linked list is singly linked list.
# ------------------------------------------------------------------------------------------------------------------------------------
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?
# ------------------------------------------------------------------------------------------------------------------------------------
# First solution can be to traverse the entire linked list and put it into some array/list/vector, then check palindrome by using two pointers expanding around centre.
# This would be done in 0(N), but with extra space: 0(N). This would be naive way of doing it.
# Secondly, alternate way and more optimized (avergely) but with sam asymtodic complexity will be to use stacks, as we go on iterating till middle, we populate stack with them
# and now while we again start iterating from middle of list, we can compare all those with top of stack and keep popping as they are matched.
#  If, at the end, stack is empty, then yes, it is palindrome otherwise not.
# Finally, optimal solution also depends on above idea but extends it to do second part traversal/transformation in-place, thereby reducing the space to 0(1).
# So, when we stop at the middle of list, then we can simply reverse the second part of list, that is remaining list after the middle point of list.
# and we can create a extra pointer pointing to the head of the list.
# Now, again we start from that extra as well as the middle one ptrs, we go for both one by one, while this middle point ptr goes Null along with matching values.
# At any point, if any one ptr's val not matches, then it returns False , otherwise True.
# TIME : 0(N), SPACE : 0(1)
# --------------------------------------------------------------------------------------------------------------------------------------
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            
        slow = self.reverseList(slow)
        fast = head
        
        while(slow):
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
            
        return True
    
    def reverseList(self, node):
        current = node
        previous = None
        
        while(current):
            currentNext = current.next
            current.next = previous
            previous = current
            current = currentNext
            
        return previous
