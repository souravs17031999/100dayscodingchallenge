# Program to find the intersection point of two linked lists
# ------------------------------
# APPROACH 1  - MOST OPTIMIZED APPROACH WITHOUT ANY EXTRA COMPUTATIONS
#--------------------------------
# TIME : 0(M + N), SPACE : 0(1)
# IDEA: LOGIC IS TO HAVE TWO POINTERS STARTING AT THE HEADS OF BOTH LINKED LISTS, AND THEN IF ANYONE OF THEM REACHES NONE EARLIER (EXHAUSTS),
# THEN WE NEED TO MOVE THAT POINTER TO THE OTHER HEAD OF LINKED LIST.
# THIS WAY WE KEEP REASSIGNING THE NULL REACHING POINTER TO OTHER HEAD OF LINKED LIST, IN THIS WAY THE TWO POINTERS WILL BE EQUIDISTANT
# FROM THE COLLISION POINT

class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:

    def find_intersection(self, head1, head2):
        ptr1, ptr2 = head1, head2

        while ptr1 and ptr2 and ptr1 != ptr2:

            ptr1 = ptr1.next
            ptr2 = ptr2.next

            if ptr1 == ptr2:
                print(f"Intersection node at : {ptr1.data}")
                return

            if ptr1 == None:
                ptr1 = head2

            if ptr2 == None:
                ptr2 = head1

# ------------------------------
# APPROACH 2
#--------------------------------
# Using the logic of first counting the length of both linked lists, then move the ptr of bigger linked list till the difference of both counts
# d = abs(c1 -c2), Now move both pointers of both linked lists, until they collide.
# TIME : 0(M + N), SPACE : 0(1)
# class Node:
#
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#
# # structure for linked list
# class LinkedList:
#
#
#     # function for getting SIZE of the linked list
#     def getSize(self, head):
#
#         count = 0
#         ptr = head
#         while ptr != None:
#             count += 1
#             ptr = ptr.next
#
#         return count
#
#     def find_intersection(self, head1, head2):
#
#         count1, count2 = self.getSize(head1), self.getSize(head2)
#         ptr1, ptr2 = head1, head2
#
#         if count1 > count2:
#             for i in range(count1 - count2):
#                 ptr1 = ptr1.next
#         else:
#             for i in range(count2 - count1):
#                 ptr2 = ptr2.next
#
#         while ptr1 != None and ptr2 != None:
#             if ptr1 == ptr2:
#                 print(f"Intersection point at : {ptr1.data}")
#                 return
#             ptr1 = ptr1.next
#             ptr2 = ptr2.next
#
#         return -1

# ------------------------------
# APPROACH 3
#--------------------------------
# If it is allowed to modify the basic data structure, then this solution will work in 0(M+N), where M, N is size of linked lists respectively.
# SPACE : EXTRA SPACE JUST FOR VISITED FLAG IN THE NODE structure
# class Node:
#
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.visited = False

# def find_intersection(self, head1, head2):
#     ptr1 = head1
#     while ptr1 != None:
#         if not ptr1.visited:
#             ptr1.visited = True
#         ptr1 = ptr1.next
#
#     ptr2 = head2
#     while ptr2 != None:
#         if not ptr2.visited:
#             ptr2.visited = True
#         else:
#             print(f"Intersection point : {ptr2.data}")
#             return
#         ptr2 = ptr2.next
#
#     print("No Intersection point found !")


if __name__ == '__main__':
    head1 = Node(3)
    node1 = Node(6)
    node2 = Node(9)
    head2 = Node(10)
    node4 = Node(15)
    node5 = Node(30)

    head1.next = node1
    node1.next = node2
    node2.next = node4
    node4.next = node5
    head2.next = node4
    llist = LinkedList()
    llist.find_intersection(head1, head2)
