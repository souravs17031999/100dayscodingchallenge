# Program to flatten multi level linked list so that first level comes first, second level comes second, third level comes third
# and so on in order of their linkage

# IDEA: We can clearly observe that we need to process one by one every node and check if it has a child, then process their child and then check again....
# optimised Logic is to traverse over each node and if it has a child, then append it's starting head to the end of the previous level (first level) of
# the list so that all others following it will be automatically in order added, now we also need to keep a tail pointer so that addition of these element
# is done in 0(1) time and then, we just update this tail pointer to that last node of child's level traversal.
# so that next time, we start traversing and keep on checking for every node in this way.
# TIME : 0(N), BECAUSE WE PROCESS ONE NODE ALL ONCE, SPACE : EXTRA SPACE NEEDED FOR TAIL POINTER AND ONE TEMP POINTER

#----------------------------------------------------
# [10] -> [5] -> [12] -> [7] -> 11                        10 -> 5 - > 12 -> 7 -> 11 ->     =>  
#  |                      |                                ^                      ^ 
#  [4] -> [20] -> [13]    [17] -> [6]                       ptr                  tail  
#          |       |       |                           => 
#         [2]     [16]    [9] -> [8]
#                   |      |
#                 [3]     [19] -> [15]
#----------------------------------------------------
#
# 10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 -> 
#  ^                                      ^
# 10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 -> 
#       ^                                 ^
# 10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 -> 
#             ^                           ^
# 10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 ->         => 10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 -> 17 -> 6 ->  [second level completely merged into first level]
#                  ^                      ^                                ^
# Similarly, for other levels.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.child = None

class LinkedList:

    def flatten(self, head):
        # Base case
        if not head:
            raise Exception ("Linked list is empty !!")
            return

        ptr, tail = head, head

        # moving tail pointer to the end of first level of list
        while tail.next:
            tail = tail.next

        # processing every node until we run out of node
        while ptr:
            # if there is a child , then add that and process that child
            if ptr.child:
                # adding child to end of the current flattening list
                tail.next = ptr.child
                temp = ptr.child
                # processing child's list so that we can get the address of the last node in this level
                while temp.next:
                    temp =  temp.next
                # updating our tail pointer to point to the last node of this level
                tail = temp

            ptr = ptr.next


    # printing the linked list
    def pretty_print(self, head):

        if not head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = head
        while ptr != None:
            print(ptr.data, end = "->")
            ptr = ptr.next

# driver function
if __name__ == '__main__':

    head = Node(10)
    node1 = Node(5)
    node2 = Node(12)
    node3 = Node(7)
    node4 = Node(11)
    node5 = Node(4)
    node6 = Node(20)
    node7 = Node(13)
    node8 = Node(17)
    node9 = Node(6)
    node10 = Node(2)
    node11 = Node(16)
    node12 = Node(9)
    node13 = Node(8)
    node14 = Node(3)
    node15 = Node(19)
    node16 = Node(15)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    head.child = node5
    node3.child = node8

    node5.next = node6
    node6.next = node7

    node8.next = node9

    node6.child = node10
    node7.child = node11
    node8.child = node12

    node12.next = node13

    node11.child = node14
    node12.child = node15

    node15.next = node16

    llist = LinkedList()
    llist.flatten(head)
    llist.pretty_print(head)
