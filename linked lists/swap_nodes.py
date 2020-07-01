# Program for swapping the nodes pairwise -
# Here, we are just swapping the nodes values of both adjacent nodes
# We can also actually change pointers / links if swapping values are not allowed.
# TIME : 0(N), SPACE : 0(1)

# Node structure class
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

# LinkedList class
class LinkedList:

    def swap_nodes(self, head):
        ptr = head
        while ptr and ptr.next :
            ptr.data, ptr.next.data = ptr.next.data, ptr.data
            ptr = ptr.next.next

        return head

    def pretty_print(self, head):
        ptr = head
        while ptr:
            print(ptr.data, end = " -> ")
            ptr = ptr.next


# driver testing function
if __name__ == '__main__':
    llist = LinkedList()
    head = Node(1)
    second1 = Node(2)
    third1 = Node(3)
    fourth1 = Node(4)
    fifth1 = Node(5)
    sixth1 = Node(6)
    seventh1 = Node(7)
    head.next = second1
    second1.next = third1
    third1.next = fourth1
    fourth1.next = fifth1
    fifth1.next = sixth1
    sixth1.next = seventh1

    llist.pretty_print(head)
    new_head = llist.swap_nodes(head)
    print()
    llist.pretty_print(new_head)
