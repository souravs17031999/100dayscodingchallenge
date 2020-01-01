# importing main linked list questions
from linkedlist import LList, Node

# funnction for deleting multiple occurences of some given value from linked list
# logic is to firstly delete all the multiple occurences of head (if to be deleted), then , delete if that val also occurs in between the list, in which we can again differ in two cases, one in which it is at last, one in which is in between repeating / non repeating.
def delete_val(head, x):
    # if there is no head
    if not head:
        return
    # if there is only one element and it is same as the given element to be deleted
    if head.data == x and head.next == None:
        head = None
        return
    # deleting head multiple occurences and finally adjust it's position
    ptr = head
    while(ptr and ptr.data == x):
        head = head.next
        ptr = ptr.next
    ptr = head
    # now, if there is no other element left, then simply return
    if ptr == None:
        return
    # otherwise, delete all other values from between the list
    while(ptr.next):
        # if that element is at last
        if ptr.next.data == x and ptr.next.next == None:
            ptr.next = None
            return head
        # if that element is in between
        elif ptr.next.data == x:
            temp = ptr.next.next
            ptr.next = temp
        # otherwise, simply increment the pointer
        else:
            ptr = ptr.next
    return head
# one more logic with same complexity is to be able to create a dummy node , so that we can check for next node's value to be able to maintain same invariant for loop so that we are always at one node previous to node to be deleted.
# dummy node is to be added to start of list 

# main function
if __name__ == '__main__':
    l = LList()
    head = Node(7)
    l.add_node_end(head, 2)
    l.add_node_end(head, 3)
    l.add_node_end(head, 2)
    l.add_node_end(head, 8)
    l.add_node_end(head, 8)
    l.add_node_end(head, 8)
    l.add_node_end(head, 8)
    l.add_node_end(head, 1)
    l.add_node_end(head, 2)
    l.add_node_end(head, 2)
    l.print_list(head) # 2->3->2->8->8->8->8->1->2->2
    head = delete_val(head, 8)
    print()
    l.print_list(head) # 2->3->2->1->2->2
