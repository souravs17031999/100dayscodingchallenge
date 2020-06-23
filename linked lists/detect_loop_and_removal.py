# Program to detect the loop in the linked list and remove it so that it longer contains a cycle
# This is the opitmized version of floyd's cycle detection algorithm and also can be applied when modification of basic structure of linked list node is not allowed.

class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

class linked_list:

    def detectAndRemoveLoop(self, head):
        flag = 0
        slow_ptr = fast_ptr = head
        while slow_ptr and fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if slow_ptr == fast_ptr:
                flag = True
                break

        if flag:
            if slow_ptr == fast_ptr:
                slow_ptr = head
                while slow_ptr.next != fast_ptr.next:
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next

                fast_ptr.next = None
                return True
        else:
            print("LOOP NOT FOUND !")
            return False

# alternate method which uses visited flag logic and can be only used when it is allowed to change the basic structure of linked list
# class Node:
#
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.visited = False
#
# class linked_list:
#
#     def detectAndRemoveLoop(self, head):
#         slow_ptr = ptr = head
#         while slow_ptr and ptr:
#
#             if not ptr.visited:
#                 ptr.visited = True
#             else:
#                 slow_ptr.next = None
#                 return True
#
#             slow_ptr = ptr
#             ptr = ptr.next
#
#         return False



if __name__ == '__main__':
    head = Node(1)
    node2 = Node(2)
    head.next = node2
    node3 = Node(3)
    node2.next = node3
    node4 = Node(4)
    node3.next = node4
    node5 = Node(5)
    node4.next = node5
    node5.next = node2  # here we explicitly point node5 to node2 to make a loop 
    llist = linked_list()
    print(llist.detectAndRemoveLoop(head))
    print(node5.next)  # this confirms that node5 no longer points to node2
