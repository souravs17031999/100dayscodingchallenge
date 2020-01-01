# program for reversing the linked lists using stacks
from linkedlist import Node, LList

# logic is to simply create a empty list and append elements of Node type directly into stack so that when we pop, we get it;s address to be put into next of new nodes contanining.
# now, keep popping and appending it to end of newly created list and keeping a pointer always to last of list.
# function for reversing the linked lists

def reverse_stack(head):
    stack = []
    ptr = head
    # pushing into stack till all elements of type Node is pushed
    while(ptr.next):
        stack.append(ptr)
        ptr = ptr.next
    # then, we make last element as head of new list
    head = ptr
    # keep popping till stack is empty and all elements are appended to the end of new list whose head is the actual last element of original list , so maybe we are taking extra space for creating new pointers, but also after exhausting stack, those original pointers are being deleted by python compiler, thereby it is not much big issue.
    # But space taken by stack is of some issue when lists are much big.
    while(stack):
        ptr.next = stack.pop()
        ptr = ptr.next
    ptr.next = None
    return head

if __name__ == '__main__':
    l = LList()
    head = Node(0)
    l.add_node_end(head, 1)
    l.add_node_end(head, 2)
    l.add_node_end(head, 3)
    l.print_list(head)
    head = reverse_stack(head)
    l.print_list(head)
