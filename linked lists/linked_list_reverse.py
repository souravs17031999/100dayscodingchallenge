class Node:
    '''
    creating this structure class will yield a address of the created node
    we can also change this using custom __repr__ method.
    '''
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:

    # head initalised to None
    def __init__(self):
        self.head = None

    # insertion at the end of linked list
    def push(self, x):

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


    # deletion at the end
    def pop(self):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = self.head
        while ptr.next.next != None:
            ptr = ptr.next

        ptr.next = None


    # searching for the element in the linked list
    def search(self, x):

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


    # function for reversing the linked list in 0(N) using three pointer approach
    # here we can also try to avoid one of the pointers named "fast_ptr" and use XOR swapping trick
    # which may or may not be space optimised but time complexity bounds will be same as it was before.
    # Space optimization here in this trick is highly architechutre dependent.



    def reverse_list(self):

        if not self.head:
            raise Exception ("Linked list is empty !!")
            return

        slow_ptr = None
        curr_ptr = self.head

        while curr_ptr:
            fast_ptr = curr_ptr.next
            curr_ptr.next = slow_ptr
            slow_ptr = curr_ptr
            curr_ptr = fast_ptr


        self.head = slow_ptr


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    # llist.push(3)
    # llist.push(4)
    # llist.push(5)
    print("Before reversing : ")
    llist.pretty_print()
    print("\nafter reversing : ")
    llist.reverse_list()
    llist.pretty_print()
