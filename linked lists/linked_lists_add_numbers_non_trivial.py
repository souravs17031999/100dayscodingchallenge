# Program to add two numbers given in linked lists representation form but in non trvial way
# so, now MSB is first node, LSB is last node (usually what is followed in normal decimal representation).
# IDEA: NAIVE SOLUTION IS TO LOGIC IS TO REVERSE LISTS GIVEN TO US, AND THEN, AFTER APPLYING SAME LOGIC
# FINALLY, REVERSE THE LIST AFTER ADDITION SO THAT OVERALL SUM IS REVERSED WHICH IS REQUIRED OUTPUT.
# TIME : 0(MAX(M, N)), SPACE : 0(1)
# WHAT IF REVERSING LIST IS PROHIBITED ? WE CAN'T MODIFY THE INPUT LISTS, THEN HOW TO OPTIMIZE ?

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

def reverse_list(head):

    if not head:
        return

    slow_ptr = None
    curr_ptr = head

    while curr_ptr:
        fast_ptr = curr_ptr.next
        curr_ptr.next = slow_ptr
        slow_ptr = curr_ptr
        curr_ptr = fast_ptr

    head = slow_ptr
    return head

def compute_sum(head1, head2):

    head1 = reverse_list(head1)
    head2 = reverse_list(head2)
    # setting pointers to both of first nodes of both linked lists
    ptr1, ptr2 = head1, head2
    carry = 0  # initalising carry to be 0

    head, last = None, None  # initalising head and last pointer to None
    # iterating while one of them exhausts
    while ptr1 or ptr2:

        # here, we are using two another variables so as to not change the actual ptr values
        # also, this is a check to ensure if any list get ehausted, then we do not encounter any error due to NoneType pointer pointing to nothing
        # so, we make it's value to be '0'
        x = ptr1.data if ptr1 != None else 0
        y = ptr2.data if ptr2 != None else 0

        # actual sum is computed using divmod logic : result is modulus, and carry is divison
        temp = x + y + carry
        head, last = Insert_Node(head, last, temp%10)
        carry = temp // 10

        # to comply with previous checks , it is needed here for the same reason.
        if ptr1 != None:
            ptr1 = ptr1.next

        if ptr2 != None:
            ptr2 = ptr2.next


    # if there is remaining carry at the last , simply add it to the answer(sum)
    if (carry):
        head, last = Insert_Node(head, last, carry)

    head = reverse_list(head)
    return head

def Insert_at_beginning(head, x):

    if not head:
        new_node = Node(x)
        head = new_node
        return

    new_node = Node(x)
    new_node.next = head
    head = new_node
    return head



# ALTERNATE METHOD : THIS APPROACH IS USED IF WE ARE NOT ALLOWED TO MODIFY INPUT LISTS,
# WE CONVERT LINKED LISTS ELEMENTS, INTO INTEGERS
# AND THEN, WE SUM UP THE RESULT (BE CAREFUL FOR OVERFLOW, BUT NOT IN PYTHON)
# THEN WE SIMPLY GET INDIVIDUAL DIGITS AND CONVERT THEM INTO NODES, RETURN THE HEAD OF
# NEW LINKED LISTS
# TIME : 0(MAX(M, N)), SPACE : 0(SOME CONSTANT SPACE)
def addTwoNumbers(l1: Node, l2: Node) -> Node:
    first_num, second_num = 0, 0
    while l1:
        first_num *= 10
        first_num += l1.data
        l1 = l1.next

    while l2:
        second_num *= 10
        second_num += l2.data
        l2 = l2.next

    result = first_num + second_num
    head = None
    if result == 0:
        head = Insert_Node(head, 0)
        return head

    while result > 0:
        head = Insert_Node(head, result % 10)
        result = result // 10

    return head


if __name__ == '__main__':
    head1 = Node(7)
    second1 = Node(2)
    third1 = Node(4)
    fourth1 = Node(3)
    head1.next = second1
    second1.next = third1
    third1.next = fourth1


    head2 = Node(5)
    second2 = Node(6)
    third2 = Node(4)
    head2.next = second2
    second2.next = third2

    head = addTwoNumbers(head1, head2)

    print(head)
    print(head.data)
    print(head.next.data)
    print(head.next.next.data)
    print(head.next.next.next.data)
