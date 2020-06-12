# program to implement linked list representation of lists in python

# node structure which consists two things - one is data (value it contains) and other is next (the address it contains for the next node)
# there are two special pointers named as head which points to beginning of list , also sometimes we can call it as root and the other is tail which points to last / end of list. We can try to use both or either of them based on the question.

# node class
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# linkedlist class
class LList:
    # intialising the lists with null head pointer
    def __init__(self):
        self.head = None

    # adding a node at the end of list
    def add_node_end(self, head, x):
        new_node = Node(x)
        if head == None:
            head = new_node
            return

        ptr = head
        while(ptr.next != None):
            ptr = ptr.next
        ptr.next = new_node
        return head

    # adding the node at the front
    def add_node_front(self, head, x):
        new_node = Node(x)
        if head == None:
           head = new_node
           return head
        new_node.next = head
        head = new_node
        return head

    # adding the node after the given value
    def add_node_after(self, head, x, y):
        new_node = Node(x)
        if head == None:
           head = new_node
           return head
        ptr = head
        while(ptr.data != y and ptr.next != None):
            ptr = ptr.next
        new_node.next = ptr.next
        ptr.next = new_node
        return head

    # deleting the node from the front
    def delete_front(self, head):
        if head == None:
            return
        else:
            head = head.next
            return head

    # deleting the node from the end
    def delete_end(self, head):
        if head == None:
            return
        else:
            ptr = head
            while(ptr.next.next != None):
                ptr = ptr.next
            ptr.next = None
        return head

    # deleting the node after soem given value
    def delelte_after(self, head, x):
        if head == None:
            return
        if head.data == x:
            head = head.next
            return head
        ptr = head
        while(ptr.next != None and ptr.next.data != x):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head

    # printing the entire linked list
    def print_list(self, head):
        if head == None:
            print('nothing in here !')
        else:
            ptr = head
            while(ptr != None):
                print(ptr.data, end = "->")
                ptr = ptr.next
            print('None')

# testing some functions by creating object of linkedlist class
if __name__ == '__main__':
    l = LList()
    root = Node(0)
    root = l.add_node_end(root, 1)
    root = l.add_node_end(root, 2)
    root = l.add_node_end(root, 3)
    l.print_list(root)
    #root = l.delete_end(root)
    #l.print_list(root)
    #root = l.delete_front(root)
    #l.print_list(root)
    root = l.delelte_after(root, 2)
    l.print_list(root)
