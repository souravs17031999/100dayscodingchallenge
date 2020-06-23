# Program for constructing and maintaining circular linked lists
# complexity asymtodic bounds are pretty much similar to what we have seen in single linked list/double linked lists

# structure node class
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

# class for circular_linked_lists
class circular_linked_lists:

    def __init__(self):
        self.head = None

    # function for inserting the node after the list (end of list)
    def push(self, x):

        if not self.head:
            new_node = Node(x)
            new_node.next = new_node
            self.head = new_node
            return

        new_node = Node(x)
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next

        ptr.next = new_node
        new_node.next = self.head

    # printing the traversal of circular_linked_lists
    # now here, the things are little tricky as we have to keep a note of starting point of traversal,
    # wherein single/double linked lists, we always have convention to start from head and then traverse till last,
    # in circular_linked_lists, we can start from any node (including head), and can traverse the entire list as the list is circular.
    def pretty_print(self, starting_point):
        # base case when linked list is empty
        if not self.head:
            raise Exception ("Linked lists empty !")
            return

        # initialising the ptr (temporary pointer) to head
        ptr = self.head

        # firstly we move to starting point and then stop there
        while ptr.data != starting_point and ptr.next != self.head:
            ptr = ptr.next

        # now we start traversing from starting point (considering it as head)
        while ptr.next.data != starting_point:
            print(ptr.data, end = "->")
            ptr = ptr.next
        print(ptr.data)

# driver function
if __name__ == '__main__':

    cllist = circular_linked_lists()
    cllist.push(0)
    cllist.push(1)
    cllist.push(2)
    cllist.push(3)
    cllist.pretty_print(2)  # 2->3->0->1
    # printing from different starting points can have different representations
