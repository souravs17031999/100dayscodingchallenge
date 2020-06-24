# Program to clone a doubly linked list where one of the pointer is similar to next but the other pointer is a random pointer pointing
# to any random pointer (maybe pointing to self node)
# IDEA: logic is to duplicate the every node and insert at its corresponding position, then, we have list of double it's original size, which consist of
# original list and newly inserted nodes
# Then, we need to get random nodes which can be fetched in 0(1) time by using orignal.next.random = original.random.next
# Now, we need to simply detach our newly cloned list against original input list so that we do not modify original list given to us in the form of input.
# Below is most optimized version in TIME : 0(N), N IS SIZE OF LINKED LIST, SPACE : 0(1)

class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None


# structure for linked list
class LinkedList:

    def clone(self, head):
        # Base class
        if not head:
            raise Exception ("Linked list is empty !!")
            return

        # copying node value and inserting the node at the correct position
        ptr = head
        while ptr:
            node = Node(ptr.data)
            node.next = ptr.next
            ptr.next = node
            ptr = ptr.next.next

        # adjusting random pointers
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        # detaching the new cloned list from original list
        ptr = head
        temp = head.next
        dummy = temp
        # here, we cannot use ptr = ptr.next, ptr = ptr.next.next for traversal as it will change the original pointers
        # because ptr is used to set here for correct addresses
        # Now, for that we also keep a temp pointer which helps us in fixing it
        # (can also be done by using more extra pointers but that would be inefficient considering optimized space)
        while ptr.next:
            temp = ptr.next
            ptr.next = ptr.next.next
            ptr = temp

        return dummy

    # printing the linked list
    def pretty_print(self, head):

        if not head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = head
        while ptr != None:
            print(f"data : {ptr.data} , random : {ptr.random.data}; ", end = "")
            ptr = ptr.next



#------------------
# APPROACH - 2
# USING IDEA OF HASHING
#---------------------
# def clone(self, head):
#
#     if not head:
#         raise Exception ("Linked list is empty !!")
#         return
#
#     ptr = head
#     count = 0
#     LinkedList.Position_MAP[count] = ptr.random
#     new_head = Node(ptr.data)
#     temp = new_head
#     ptr = ptr.next
#
#     while ptr:
#         node = Node(ptr.data)
#         temp.next = node
#         temp = node
#         count += 1
#         LinkedList.Position_MAP[count] = ptr.random
#         ptr = ptr.next
#
#     ptr = new_head
#     count = 0
#     while ptr:
#         ptr.random = LinkedList.Position_MAP[count]
#         count += 1
#         ptr = ptr.next
#
#     return new_head, LinkedList.Position_MAP

# driver function
if __name__ == '__main__':
    head = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    head.random = node2
    node1.random = head
    node2.random = node4
    node4.random = node1
    node3.random = node2

    llist = LinkedList()
    llist.pretty_print(head)
    print()
    new_head = llist.clone(head)
    llist.pretty_print(new_head)
