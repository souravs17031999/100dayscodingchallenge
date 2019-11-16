class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LList:
    def __init__(self):
        self.head = None

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


    def add_node_front(self, head, x):
        new_node = Node(x)
        if head == None:
           head = new_node
           return head
        new_node.next = head
        head = new_node
        return head

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

    def delete_front(self, head):
        if head == None:
            return
        else:
            head = head.next
            return head

    def delete_end(self, head):
        if head == None:
            return
        else:
            ptr = head
            while(ptr.next.next != None):
                ptr = ptr.next
            ptr.next = None
        return head

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

    def print_list(self, head):
        if head == None:
            print('nothing in here !')
        else:
            ptr = head
            while(ptr != None):
                print(ptr.data, end = "->")
                ptr = ptr.next
            print('None')
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
