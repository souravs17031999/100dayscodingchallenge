# Program for constructing for singly linked list
# TIME FOR INSERTION AT END : 0(N), TIME FOR INSERTION AT BEGINNING : 0(1)
# TIME FOR DELETION AT END : 0(N), TIME FOR DELETION AT BEGINNING : 0(1)
# TIME FOR lookup : 0(N)
# WHERE N IS SIZE OF THE LENGTH LIST

# structure for node
# this contains data which is the value for node
# and next which contains address of the next node
class Node:
    '''
    creating this structure class will yield a address of the created node
    we can also change this using custom __repr__ method.
    '''
    def __init__(self, x):
        self.data = x
        self.next = None

# structure for linked list
class LinkedList:

    # head initalised to None
    def __init__(self):
        self.head = None

    # insertion at the end of linked list
    def insert_at_end(self, x):

        # base case when there is no node present , then we simply create a new node
        # and set it as head
        if not self.head:
            new_node = Node(x)
            self.head = new_node
            return

        # in other cases, we traverse to that last node and then attach new node at the end
        ptr = self.head
        new_node = Node(x)
        while ptr.next != None:
            ptr = ptr.next

        ptr.next = new_node

    #  inseting at the head
    def insert_at_head(self, x):

        if not self.head:
            new_node = Node(x)
            self.head = new_node
            return

        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    # insetion after given position (after element)
    def insert_after_position(self, x, pos):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = self.head
        while ptr.data != pos and ptr.next != None:
            ptr = ptr.next

        new_node = Node(x)
        new_node.next = ptr.next
        ptr.next = new_node

    # insertion before position (before given element)
    def insert_before_position(self, x, pos):
        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        if self.head.data == pos:
            self.insert_at_head(x)
            return

        ptr = self.head
        while ptr.next.data != pos and ptr.next != None:
            ptr = ptr.next

        new_node = Node(x)
        new_node.next = ptr.next
        ptr.next = new_node

    # deletion at the end
    def delete_at_end(self):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = self.head
        while ptr.next.next != None:
            ptr = ptr.next

        ptr.next = None

    # deletion at the head
    def delete_at_head(self):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        temp = self.head
        self.head = self.head.next
        temp = None

    # deletion at the given position
    def delete_at_pos(self, pos):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = self.head
        while ptr.next.data != pos:
            ptr = ptr.next

        temp = ptr.next
        ptr.next = ptr.next.next
        temp = None

    # searching for the element in the linked list
    def lookup(self, x):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = self.head
        while ptr != None:
            if ptr.data == x:
                return "Element found in the list !"
            ptr = ptr.next

        return "Element not found"

    # function for getting SIZE of the linked list
    def getSize(self):

        count = 0
        ptr = self.head
        while ptr != None:
            count += 1
            ptr = ptr.next

        return count

    # method for getting element at index position accessing
    def getElement(self, pos):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        if pos > self.getSize():
            raise Exception ("Index access out of bounds !!")
            return

        ptr = self.head
        for i in range(pos):
            ptr = ptr.next

        return ptr.data

    # printing the linked list
    def pretty_print(self):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = self.head
        while ptr != None:
            print(ptr.data, end = "->")
            ptr = ptr.next



# driver function for testing above function
if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_end(0)
    llist.insert_at_end(1)
    llist.insert_at_end(2)
    llist.insert_at_head(10)
    llist.insert_after_position(99999, 11)
    llist.insert_before_position(345, 99999)
    llist.insert_before_position(-500, 10)
    print("List before deletion at tail : ")
    llist.pretty_print()
    llist.delete_at_end()
    print("\nList after deletion : ")
    llist.pretty_print()
    print("\nList after deletion of head: ")
    llist.delete_at_head()
    llist.pretty_print()
    llist.delete_at_pos(1)
    print("\nList after deletion of 1:")
    llist.pretty_print()
    llist.pretty_print()
    print("\nSearching for element : 1")
    print(llist.lookup(100))
    llist.pretty_print()
    print(f"\nElement at index 1 : {llist.getElement(0)}")
    
