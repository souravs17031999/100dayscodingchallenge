# Sorting based on simple key parameters (array)
# -----------------------------------------------------------------------------------

# sorting by keys
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
# list sorting by second index or first index
list.sort(key = lambda x : x[0])
# print(list)  # [['Alice', 86], ['Bob', 99], ['Eve', 78], ['Suzy', 86]]

# Sorting by multiple keys -> first by first index, and then by second index
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]

list.sort(key = lambda x : (x[1], x[0]))

# print(list)

# reversing order for both keys
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
list.sort(key = lambda x : (x[1], x[0]), reverse=True)
# print(list)

# ---------------------------------------------------------------------------------------

# Faster approach :
from operator import itemgetter
list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
list.sort(key = itemgetter(1, 0), reverse=True)
# print(list)
# above only reversed for both keys but we only want to do for one of the keys.



# FOR MORE ADVANCED comparators WHICH HAVE MORE BETTER CONTROL
# ------------------------------------------------------------------------------------------
# PART 1:

# Using custom comparators
import functools
def numeric_compare(x, y):
    return x[1] - y[1]

def reverse_compare(x, y):
    return y[1] - x[1]


list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
list.sort(key = functools.cmp_to_key(numeric_compare)) # can also pass reverse_compare same way.
# print(list)

# PART 2:

strings = "here are Some sample strings to be sorted".split()

# first on length, then on only upper chars
def mykey(x):
    return -len(x), x.upper()

print sorted(strings, key=mykey)

# PART 3:
# Now, let's say we want to group some chars like only uppercase chars, and then perform the sort based on that only.
# For custom caparators, we always want to return 1, -1.


def ord_compare(x, y):
    first = []
    second = []
    for i in x:
        if i.isupper():
            first.append(i)

    for i in y:
        if i.isupper():
            second.append(i)

    first = "".join(first)
    second = "".join(second)
    if first >= second:
        return 1
    else:
        return -1

res.sort(key = cmp_to_key(ord_compare))

#
# # now if we want to reverse order for only one of the key and not for the other.
#
# list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
# list.sort(key = lambda x : (-x[1], x[0])) # only works if number is to be reversed , can be done by multilpying by -1
# print(list)
#
# # list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
# # list = sorted(sorted(list, key = lambda x : -x[1]), key = lambda x : x[0])
# # print(list)
#
# # if input -> is in string.
# list = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
# list.sort(key = lambda x : (-int(x[1]), x[0])) # only works if number is to be reversed , can be done by multilpying by -1
# print(list)
