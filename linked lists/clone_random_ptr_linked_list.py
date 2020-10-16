# Program to clone a doubly linked list where one of the pointer is similar to next but the other pointer is a random pointer pointing
# to any random pointer (maybe pointing to self node)

# Firstly, we need to carefully understand the question because it's not trivial to find the random ptr here and map it, because once we are at some position
# in the linked list (singly), we can't move back or jump ahead for mapping random pointers.
# IDEA: So, first idea that comes to mind is to use some kind of hashing so improve these accesses (which are expensive for random ptr to move around)
# so that mapping would be easier. So, we create a hashMap where key is original node add, and value is cloned node add.
# Now, again we traverse the original linked list, and create the wirings for both next and random using the hashtable becasue we can simply adjust the ptr
# as we have saved them in the hashMap.
# TIME : - 0(N), SPACE : 0(N)

# Efficient, logic is to duplicate the every node and insert at its corresponding position, then, we have list of double it's original size, which consist of
# original list and newly inserted nodes
# Then, we need to get random nodes which can be fetched in 0(1) time by using original.next.random = original.random.next
# Now, we need to simply detach our newly cloned list against original input list so that we do not modify original list given to us in the form of input.
# Below is most optimized version in TIME : 0(N), N IS SIZE OF LINKED LIST, SPACE : 0(1)
# Old List: A --> B --> C --> D
# InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
# Now, we can see below diagram for better intution about setting random pointers :
#    _________________________
#   |                         |
#   A --> A' --> B --> B' --> C --> C' --> D --> D'
#  In the above linked list, random ptr of A points to C, so, what is original.random.next ? it's the copy of original.random, and so, if we see clearly, then 
#  we can point original.next.random to original.random.next as shown below : 
#    _________________________
#   |                         |
#   A --> A' --> B --> B' --> C --> C' --> D --> D'
#         |                         |
#         ---------------------------  
#
# --------------------------------------------------------------------------------------------------------------------------------------------

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
#"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return head

        map = {}
        ptr = head
        while ptr:
            map[ptr] = Node(ptr.val)
            ptr = ptr.next

        ptr = head
        while ptr:
            if ptr.next != None:
                map[ptr].next = map[ptr.next]
            if ptr.random != None:
                map[ptr].random = map[ptr.random]
            ptr = ptr.next

        return map[head]

        
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
