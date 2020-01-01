# program for deleting the node given only it's reference, not any head ref

# importing all linkedlist main functions
from linkedlist import LList, Node

# functions for deleting given node

# logic is to simply swap the given node pointer data with next node data, and then delete the next node which contains now that original data by pointing and adjusting pointer by skipping the deleted node.
def delete_val(node):
    if not node:
        return
    # swapping the current node and next node
    node.next.data, node.data = node.data, node.next.data
    # deleting the node by skipping the connection between current node and swapped node
    node.next = node.next.next

# main function 
if __name__ == '__main__':
    l = LList()
    head = Node(4)
    first_node = Node(5)
    second_node = Node(1)
    third_node = Node(9)
    head.next, first_node.next, second_node.next, third_node.next = first_node, second_node, third_node, None  # 4->5->1->9
    delete_val(first_node) # deletes 5
    ptr = head
    while(ptr):
        print(ptr.data, end = " ")
        ptr = ptr.next
    # prints 4->1->9
