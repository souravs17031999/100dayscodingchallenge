# Program for constructing the double linked lists
# idea is to store the two extra pointers pointing to one previous node and one next node
# so, using this we have adjust both the links for any insertion, deletions and updations.
# loopkup is similar to single linked lists
# asymtodic bounds are very similar to single linked lists as very little difference can be observed for space
# complexity where doubly_linked_lists can take little extra space against single liked lists
# but there is another XOR linked lists which are used to maintain doubly_linked_lists efficiently using one pointer field.

# structure for node class
class Node:

    def __init__(self, x):
        self.data = x
        self.prev = None
        self.next = None

# class structure for doubly_linked_lists
class doubly_linked_lists:

    def __init__(self):
        self.head = None


    # function for inserting the element at the end of doubly_linked_lists
    def push(self, x):

        if not self.head:
            new_node = Node(x)
            self.head = new_node
            return

        new_node = Node(x)
        ptr = self.head

        while ptr.next != None:
            ptr = ptr.next

        ptr.next = new_node
        new_node.prev = ptr


    # printing the traversal of doubly_linked_lists
    def pretty_print(self):

        if not self.head:

            raise Exception ("Linked lists empty !")

        ptr = self.head
        while ptr != None:
            print(ptr.data, end = "->")
            ptr = ptr.next

if __name__ == '__main__':

    dllist = doubly_linked_lists()
    dllist.push(0)
    dllist.push(1)
    dllist.push(2)
    dllist.push(3)
    dllist.pretty_print()
