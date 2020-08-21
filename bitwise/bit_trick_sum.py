# Just one trick to observe while we sum two different digits in differen n-base systems :
# Let's say we have 1->2 => 12
# So, what we did above was simply following :
# taking first digit and left shift by one bit and add the next digit :
# 1 * 10 + 2 = 12

# Similar approach could be followed for other systems such as binary :
# 1->1 => 3
# 1 << 1 | 1 => 3
curr_number = 1
curr_number = (1 << 1) | 1 = 3
