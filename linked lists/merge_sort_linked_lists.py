# program for merge sort two linked lists
# # IDEA: logic is to use the same idea of merging two arrays using merge sort idea
# so here we just use a dummy node to start off with and keeping a tail pointer to the recently added node to the dummy node
# So, overall we keep two pointers , one for first linked list and then for second linked list, then create a dummy node and a tail node which will point to latest added element
# so that we can keep adding element to the last of resultant linked list in 0(1) time.
# hence, we compare both the pointers, which ever is smaller, we take it off from the original list and add it to our resultant list
# when one of the list exhausts, then we simply point the tail node to the start of which ever list is remained.
# In this way we will be able to return the first node just after dummy node so that we will be using it to traverse the list
# This is the optimized space efficient solution which just uses extra space for one dummy node which is also temporary and no other extra space is required.
# IT IS ALL ABOUT MOVING POINTERS AND LINKING AT CORRECT PLACE.
# TIME : 0(N), N IS MAX(SIZE OF LINKED LIST1, SIZE OF LINKED LIST2), SPACE : JUST DUMMY NODE EXTRA SPACE
class Node:
    '''
    Structure of node class
    '''
    def __init__(self, x):

        self.data = x
        self.next = None

class linked_list:
    '''
    linked list Structure class
    '''
    def merge_sort_list(self, head1, head2):
        '''
        head1 is first head of first linked list
        head2 is second head of second linked list
        '''

        ptr1, ptr2 = head1, head2
        # dummy which is simply a point to start off and keep adding our element from either of the linked lists
        dummy = Node(-1)
        # tail helps us to keep track of pointing to the last added element
        tail = dummy
        # iterating over both linked lists until one of them exhausts
        while ptr1 != None and ptr2 != None:

            # element of first linked list is smaller so, branching it off from its original list
            # and then linking it to our resultant list
            if ptr1.data < ptr2.data:
                temp = ptr1
                tail.next = temp
                tail = temp
                ptr1 = ptr1.next
                temp.next = None
            else:
                # element of second list is smaller
                temp = ptr2
                tail.next = temp
                tail = temp
                ptr2 = ptr2.next
                temp.next = None

        # if first linked list exhausts, then simply link our result list to the second list
        if ptr1 == None:
            tail.next = ptr2
        # if second linked_list exhausts, then simply link our result list to the first list
        elif ptr2 == None:
            tail.next = ptr1

        # now we have completed our resultant list by linking all the pointers
        # hence, we return the first node after dummy
        return dummy.next

    # printing the linked list
    def pretty_print(self, head):

        if not head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = head
        while ptr != None:
            print(ptr.data, end = "->")
            ptr = ptr.next


if __name__ == '__main__':
    head1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    head1.next = node2
    node2.next = node3

    head2 = Node(0)
    node4 = Node(2)
    node5 = Node(4)
    head2.next = node4
    node4.next = node5
    llist = linked_list()
    combined_head = llist.merge_sort_list(head1, head2)
    llist.pretty_print(combined_head)
