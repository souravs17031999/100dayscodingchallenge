class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def insert(self, head, x):
        if head == None:
            new_node = Node(x)
            head = new_node
            return head

        new_node = Node(x)
        ptr = head
        while(ptr.next):
            ptr = ptr.next

        ptr.next = new_node
        return head
    def print_list(self, head):
        if not head:
            print('Empty list !')
            return
        ptr = head
        while(ptr):
            print(f"{ptr.data}->", end = " ")
            ptr = ptr.next
    def reverse_list(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        prev_node = None
        cur_node = head
        while(cur_node != None):
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        head = prev_node
        return head

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
