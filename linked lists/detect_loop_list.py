# Program to check if linked list contains a cycle / loop or not 
# Idea : First logic is that we can use a extra field in node structure named as "visited" , and mark it while traversing along the linked list 
# then, if we encounter a already visited node, then obvisoulsy, we have found a loop.
# Optimized version is called floyd's cycle detection algorithm which uses two pointers technique also called hare and tortoise algorithm
# in which one is called slow_ptr which moves one step at a time, and another known as fast_ptr which moves two steps at a a time.
# and then since the cycle length is n, they will defintely meet at some time if there is a loop.
# Time : 0(N), Space : extra space whatever is required by using two extra pointers.

def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    slowptr = fastptr = first_node
    while slowptr and fastptr and fastptr.next:
        slowptr = slowptr.next
        fastptr = fastptr.next.next
        if slowptr == fastptr:
            return True

    return False
