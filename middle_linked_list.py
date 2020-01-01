# program to find and return middle element of linked lists

# importing all functions from main linked list
from linkedlist import LList, Node

# function for middle list return
def middle_list(head):
    # if head is none
    if head == None:
        return
    # if only one element is present
    if not head.next:
        return head
    # if only two element is present
    if not head.next.next:
        return head.next
    # otherwise, use two pointers trick, so move one pointer twice as fast as the slow pointer which moves one step at a time and when fast one will reach the end of list, slow one will be at the middle of the list.
    slow_ptr = fast_ptr = head
    while(fast_ptr and fast_ptr.next):
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    return slow_ptr

# main function     
if __name__ == '__main__':
    l = LList()
    head = Node(1)
    l.add_node_end(head, 2)
    l.add_node_end(head, 3)
    l.add_node_end(head, 4)
    l.add_node_end(head, 5)
    l.add_node_end(head, 6)
    l.print_list(head)
    print(middle_list(head).data)
