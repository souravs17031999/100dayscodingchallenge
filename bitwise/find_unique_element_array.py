# Given a list of ids, find the unique ID from the list (It is guaranteed to have a unique id)
# logic is that we can try to use hashing (dictionery) to keep track of how many integers we have seen in one pass, then
# go over dictionery stored to check which one is unique.
# This approach takes time 0(N) with space 0(N)
# Another approach is to use binary level information to use fact that XOR cancels out when it sees itself and gives the result when
# some different item is taken (here, the items in list).
# This takes 0(N) time , but with also space 0(1) which makes it more optimized.

def find_unique_delivery_id(delivery_ids):
    # if list is empty
    if len(delivery_ids) == 0:
        return
    # if list contains only one element
    if len(delivery_ids) == 1:
        return delivery_ids[0]
    # otheriwse, we set a temporary variable , which is set initially to 0 which never occurs in the list.
    temp_bit = 0
    # XOR it with every item in the list will result finally in that item value which is unique because other's will cancel each other.
    for i in delivery_ids:
        temp_bit ^= i

    return temp_bit

    # array_length = len(delivery_ids)
    # max_value = max(delivery_ids)
    # count = {}
    # for i in range(array_length):
    #     if delivery_ids[i] in count:
    #         count[delivery_ids[i]] += 1
    #     else:
    #         count[delivery_ids[i]] = 1
    # for i, j in count.items():
    #     if j == 1:
    #         return i

# main function
if __name__ == '__main__':
    assert find_unique_delivery_id([1]) == 1
    assert find_unique_delivery_id([1, 2, 2]) == 1
    assert find_unique_delivery_id([3, 3, 2, 2, 1]) == 1
    assert find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1]) == 8
