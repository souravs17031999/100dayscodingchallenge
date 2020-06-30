# Program to compute sum of two numbers given in linked list representation as reversed form : LSB is first node, MSB is last node
# IDEA: logic is very similar to array digit sum problem where we move one by one simultaneously two pointers and keep adding it to
# running sum and carry and an extra carry at then end , if there is one .
# Now, here we have to slghly modify the logic according to our needs,
# first we have already two pointers to two heads and then we can keep moving until one of them exhausts , at that point we have to simulate and keep running
# by making the exhausted list element as 0 as long as one of the list's element is yet to be added for overall sum.
# So, we can keep for that.
# Also, to keep above check working, we need the same type of check, when we need to advance our pointers so that we donot advanced any NoneType pointers.
# Also, Insertion of new node to resultant linked list should be done in 0(1) , for that we can keep a "last" pointer, which will always point to the latest added node.
# TIME : 0(MAX(M, N)) , M, N IS LENGHT OF LINEKD LISTS, SPACE : 0(MAX(M, N))

# NOTE : REASON FOR SAFETY CHECKS,
# let's say : l1 : [1, 8] and l2 : [0]
# Then, out pointer will add the both elment 1 + 0 = 1 (new node created), now we advnace both the pointers, but since second list pointer is pointing to nothing (due to NoneType)
# we have make it '0' so that addition keeps going on with assuming second list element to be 0 which will not have any effect on the overall sum.

# struture of node class
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# function for inserting node using head and last pointers, since head will be
# modifed after first time, so we are returning it also
# THIS TAKES 0(1) TIME
def Insert_Node(head, last, x):
    if not head:
        new_node = Node(x)
        head = new_node
        last = head
        return head, last

    new_node = Node(x)
    last.next = new_node
    last = new_node
    return head, last

# function for adding the elements of both linked lists starting from left -> right
def sum_array(head1, head2):
    # setting pointers to both of first nodes of both linked lists
    ptr1, ptr2 = head1, head2
    carry = 0  # initalising carry to be 0

    head, last = None, None  # initalising head and last pointer to None
    # iterating while one of them exhausts
    while ptr1 and ptr2:

        temp = ptr1.data + ptr2.data + carry
        head, last = Insert_Node(head, last, temp%10)
        carry = temp // 10
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    # if list 1 is exhausted, then we can keep iterating and add up all the leftover for second list
    if ptr1 == None:
        while ptr2:
            temp = ptr2.data + carry
            head, last = Insert_Node(head, last, temp%10)
            carry = temp // 10
            ptr2 = ptr2.next
    # if list 2 is exhausted, then we can keep iterating and add up all the leftover for first list 
    if ptr2 == None:
        while ptr1:
            temp = ptr1.data + carry
            head, last = Insert_Node(head, last, temp%10)
            carry = temp // 10
            ptr1 = ptr1.next

    # if there is remaining carry at the last , simply add it to the answer(sum)
    if (carry):
        head, last = Insert_Node(head, last, carry)

    return head

def pretty_print(head):
    ptr = head
    while ptr:
        print(ptr.data, end = " -> ")
        ptr = ptr.next

if __name__ == '__main__':
    head1 = Node(1)
    second1 = Node(8)
    # third1 = Node(3)
    head1.next = second1
    # second1.next = third1

    head2 = Node(0)
    # second2 = Node(6)
    # third2 = Node(4)
    # head2.next = second2
    # second2.next = third2
    pretty_print(head1)
    print()
    pretty_print(head2)
    head = sum_array(head1, head2)
    print()
    pretty_print(head)
