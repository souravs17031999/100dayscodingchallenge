# program to reverse linked list iterative way

# class for creating nodes
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# class for linked list construction
class linked_list:
    def __init__(self):
        self.head = None

    # function for inserting nodes
    def insert(self, head, x):
        # if head doesn't exist, then return simply the newly created head
        if head == None:
            new_node = Node(x)
            head = new_node
            return head
        # otherwise, traverse to the end of list and adjust the pointer of the last node to the newly created node
        new_node = Node(x)
        ptr = head
        while(ptr.next):
            ptr = ptr.next

        ptr.next = new_node
        return head
    # function for printing linked lists
    def print_list(self, head):
        if not head:
            print('Empty list !')
            return
        ptr = head
        while(ptr):
            print(f"{ptr.data}->", end = " ")
            ptr = ptr.next
    # function for reversing lists
    # manipulating every current pointer node to point to its previous node by keeping track of next node address so that we do not lose track of next node to keep traversing in the same direction and finally when all the links are reversed, list is reversed by making the head pointing to the last pointer node.
    def reverse_list(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        # keeping three pointers prev_node, cur_node and next_node
        prev_node = None
        cur_node = head
        while(cur_node != None):
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        # returning new head
        head = prev_node
        return head

# main function
if __name__ == '__main__':
    l = linked_list()
    root = None
    root = l.insert(root, 0)
    root = l.insert(root, 1)
    root = l.insert(root, 2)
    l.print_list(root)
    root = l.reverse_list(root)
    print()
    l.print_list(root)
