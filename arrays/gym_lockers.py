# Program for computing total count of open doors (lockers) after performing following operations:
# In first pass, we open all doors,
# in second pass, we close all other door (second door),
# in third pass, we closes all third doors,
# in fourth pass, we closes all fourth doors, ..........
# How many are left open in the end.

# If we observe closesly, then it's just factors of the number (current pass) which is important,
# ex. 10
#          1 2 3 4 5 6 7 8 9 10
#  N = 1   ____________________
#  N = 2     *   *   *   *    *
#  N = 3     * * *   *   * * *
#  N = 4     ......
#  N = 5
# N = 10   _ * * _ * * * * _ *

# So, only left open lockers are the count of all perfect squares upto 10 => 1, 4, 9 (3)
# Similarly, we can generalise for all given N.

# Hence, count of open doors/lockers from given N => floor(sqrt(N))
