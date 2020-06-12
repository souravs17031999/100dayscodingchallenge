def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    slowptr = fastptr = first_node
    while slowptr and fastptr and fastptr.next:
        slowptr = slowptr.next
        fastptr = fastptr.next.next
        if slowptr == fastptr:
            return True

    return False
