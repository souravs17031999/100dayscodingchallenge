# prints breadth of s
print('---------------', end = " ")
print('--------------------------', end = " ")
print('              -', end = " ")
print('                              {}'.format(('-')*20))
j = 0
for i in range(1, 16):
    print(" "*i, end = "")
    # prints bottom part of t
    print('\\', end = " "*(30 - i))
    # prints diagonal part of s
    print('|', end = " "*(25 - i))

    print('/', end = " "*(i + j))
    j += 1

    print('\\', end = " "*(30 - i))

    print('|')


print('---------------')
# prints t

input()
