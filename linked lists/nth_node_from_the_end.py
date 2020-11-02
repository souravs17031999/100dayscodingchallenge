# Program to get nth node from the end in a linked list
# IDEA: logic is to use two same two pointer concept which says that maintain two pointers starting from head,
# firstly move one of the pointers called ref_ptr to given kth position(from the end) from the head,
# then move both the pointers one by one and then the until ref_ptr exhausts, so the other pointer will be at the kth position at the end
# TIME : 0(N), N IS LENGHT OF Linked list , SPACE : WHATEVER EXTRA SPACE THE EXTRA TWO POINTERS TAKE

class Node:

    def __init__(self, x):

        self.data = x
        self.next = None

class linked_list:

    def get_nth_node(self, head, k):
        # base case : when linked list is empty
        if not head:
            raise exception ("Linked list empty !")

        # check for invalid positions like negative indices
        ptr = ref_ptr = head
        if k <= 0:
            print("INvalid positions !")
            return
        # we can also simply use for loop to traverse ref_ptr to the kth pos from the head
        # but we also want to create a check for out of bounds position access, so we make it using while loop
        # maintaining a counter keeping a count of how many times we move (traverse) ,
        # now if count < k and let's say length of linekd list is 4, and k = 10, so what will happen is
        # ref_ptr will become None after travrsing this while loop
        count = 0
        while count < k:
            if ref_ptr is None:
                print("Given position is out of bounds !")
                return
            ref_ptr = ref_ptr.next
            count += 1

        # for other case, we are already at kth position fromt he head using ref_ptr
        # now we move both pointer until ref_ptr exhausts
        while ref_ptr != None:
            ptr = ptr.next
            ref_ptr = ref_ptr.next

        # ptr points now to the kth positioon from the end
        return ptr.data

# Deleting nth node from the end, so, actually, we need to stop one node before in order to delete next node (reqired nth node from the end).
# So, we create a dummy node, and then start the above two pointers from dummy node.
# Then, we move fast_ptr to "n + 1" times, then start both till fast_ptr goes None.
# Finally, our slow_ptr points to just before the node to be deleted, so go ahead and delete the node (kth from the end).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if head == None:
            return 
        
        if head.next == None and n == 1:
            del head
            return
        
        
        dummy = ListNode(-1)
        dummy.next = head 
        fast_ptr, slow_ptr = dummy, dummy 
        
        for i in range(n + 1):
            fast_ptr = fast_ptr.next
        
        while fast_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        
        temp = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        del temp
        return dummy.next 
    
        

if __name__ == '__main__':
    head = Node(1)
    node2 = Node(2)
    head.next = node2
    node3 = Node(3)
    node2.next = node3
    node4 = Node(4)
    node3.next = node4
    node5 = Node(5)
    node4.next = node5
    llist = linked_list()
    print(f"value of 3nd node from the end is {llist.get_nth_node(head, 3)}")
