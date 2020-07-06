# Program for deleting the node given only pointer to that node , no head reference is given
## IDEA: logic is simple : since we have reference only to current node and we can only delete a node when we are just one step back from it,
# so we copy the next element to the current element so that it imitates the next element and then, delete the next node.
# ALso, we can directly swap the addresses but that one is trciky is python as it doesn't give access to pointers explicitly.
# and also we have to free the node, so for that we can set next to None (for node deleted)
# NOTE : This will not work for nodes to be deleted is at the end of LinkedList , so for that to be worked, we can mark the end node as dummy node .
# create a dummy node and apply the same logic as above and we will finally have a LinkedList with deleted node and a extra dummy node.

# TIME : 0(1), SPACE  : 0(1)
import sys

class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

# structure for linked list
class LinkedList:

    def delete_node(self, node):

        if node.next != None:
            # ptr is pointing to next node
            ptr = node.next
            # copying the next element value to current value
            node.data = ptr.data
            # directly linking current element to the next to next element , bypassing next element (which is now node to be deleted)
            node.next = ptr.next
            # now, setting next node (node which is deleted) to None
            ptr.next = None
            return

        # This case should be there if we also want to delete last node - by introducting dummy node
        # but this will affect other programs using this, hence we should also modify other programs according to it.
        # dummy = Node(sys.maxsize)
        # node.next = dummy
        # node.data = dummy.data
        # node.next = None
        # del dummy


    # printing the linked list
    def pretty_print(self, head):

        if not head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = head
        while ptr:
            print(ptr.data, end = "->")
            ptr = ptr.next

# driver function
if __name__ == '__main__':
    head = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    llist = LinkedList()
    llist.pretty_print(head)
    llist.delete_node(node4)
    print()
    llist.pretty_print(head)
