# We need to design the linked list data struture for supporting the following operations.
# We can use singly linked list or doubly linked list containing val, next and val, next, prev respectively.
# Implement following functions :
# ----------------------------------------
# *get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# *addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion,
# the new node will be the first node of the linked list.
# *addAtTail(val) : Append a node of value val to the last element of the linked list.
# *addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to
# the length of linked list, the node will be appended to the end of linked list. If index is greater than the
# length, the node will not be inserted.
# *deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
# ---------x-----------------x------------
# Approach : We can also include "size" as a another attribute in the structure of Node.
# But here it is not allowed, so we will use simple operations running mostly in linear time (maybe more than single pass) !
# ---------x-----------------x------------
class Node:

    def __init__(self, data):
        self.val = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def getSize(self) -> int:
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.getSize():
            return -1

        ptr = self.head
        i = 0
        while ptr and i != index:
            i += 1
            ptr = ptr.next

        return ptr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            new_node = Node(val)
            self.head = new_node

        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            new_node = Node(val)
            self.head = new_node
        else:
            ptr = self.head
            new_node = Node(val)
            while ptr.next:
                ptr = ptr.next

            ptr.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.getSize():
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.getSize():
            self.addAtTail(val)
            return

        ptr = self.head
        i = 0
        while ptr.next and (i + 1) != index:
            i += 1
            ptr = ptr.next

        new_node = Node(val)
        new_node.next = ptr.next
        ptr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is None:
            return

        if index >= self.getSize():
            return

        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp = None
            return

        ptr = self.head
        i = 0
        while ptr.next and (i + 1) != index:
            i += 1
            ptr = ptr.next

        temp = ptr.next
        ptr.next = ptr.next.next
        temp.next = None

    def printLinkedList(self):
        ptr = self.head
        while ptr:
            print(ptr.val, end = " -> ")
            ptr = ptr.next
        print()

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
print(obj.getSize())
obj.addAtIndex(3, 0)
obj.printLinkedList()
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
print(obj.get(4))
