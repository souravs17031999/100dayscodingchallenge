# sorting by keys
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
# list sorting by second index or first index
list.sort(key = lambda x : x[0])
# print(list)  # [['Alice', 86], ['Bob', 99], ['Eve', 78], ['Suzy', 86]]

list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]

list.sort(key = lambda x : x[1])
# print(list) # [['Eve', 78], ['Suzy', 86], ['Alice', 86], ['Bob', 99]]

# Sorting by multiple keys -> first by first index, and then by second index
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]

list.sort(key = lambda x : (x[1], x[0]))

# print(list)

# reversing order for both keys
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
list.sort(key = lambda x : (x[1], x[0]), reverse=True)
# print(list)

# Faster approach :
from operator import itemgetter
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
list.sort(key = itemgetter(1, 0), reverse=True)
# print(list)
# above only reversed for both keys but we only want to do for one of the keys.

# Using custom comparators
import functools
def numeric_compare(x, y):
    return x[1] - y[1]

def reverse_compare(x, y):
    return y[1] - x[1]


list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
list.sort(key = functools.cmp_to_key(numeric_compare)) # can also pass reverse_compare same way.
# print(list)


# now if we want to reverse order for only one of the key and not for the other.

list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
list.sort(key = lambda x : (-x[1], x[0])) # only works if number is to be reversed , can be done by multilpying by -1
print(list)

# list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
# list = sorted(sorted(list, key = lambda x : -x[1]), key = lambda x : x[0])
# print(list)

# if input -> is in string.
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
list.sort(key = lambda x : (-int(x[1]), x[0])) # only works if number is to be reversed , can be done by multilpying by -1
print(list)
