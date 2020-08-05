# Program for sequencing the job schedule for maximizing the profit associate with the deadline.
# ------------------------------------------------------------------------------
# JobID  Deadline  Profit
#   a      4        20
#   b      1        10
#   c      1        40
#   d      1        30
# -------------------------------------------------------------------------------
# Now, here, we can think that the optimal substructure property -> local optimal
# problems will lead us to overall optimal problems.
# We will try to use greedy approach to find the best possible profit at current moment,
# also we will try to schedule jobs more to the last slot avaiable.
# Because scheduling early will be of no help, scheduling later will be of good help as
# there can be more jobs later on which can scheduler early on, so we will not miss those jobs.
# --------------------------------------------------------------------------------
# We can maintain slots to be filled from the last possible available slot and hence try to
# schedule all the jobs after sorting the jobs on profit.
# ---------------------------------------------------------------------------------
# So, in the above example, profit sorted :
# 40 30 20 10
# 1   1  4  1
# c   d  a  b
# So, c, a => 60 is the maximum profit as slots available 4.
#  --------------------------------------------------------------------------------
# input given :
# arr = [['a', 2, 100], # Job Array
#        ['b', 1, 19],
#        ['c', 2, 27],
#        ['d', 1, 25],
#        ['e', 3, 15]]
# ---------------------------------------------------------------------------------
# TIME : 0(N^2)
# ----------------------------------------------------------------------------------
def sequence_job(arr, t):

    # sorting the array reverse (descending order on profit )
    arr.sort(key = lambda x : x[2], reverse=True)
    print(arr)
    result = [-1] * t
    slots = [True] * t
    # going for all jobs
    for i in range(len(arr)):

        # finding the best position from the end
        # here we actually use 0-based indexing, so arr[i][1] - 1 is considered
        for j in range(min(arr[i][1] - 1, t - 1), -1, -1):
            # if empty slot is available
            if slots[j] is True:
                result[j] = arr[i][0]
                slots[j] = False
                break

    # print only the filled slots jobs
    for i in range(len(arr)):
        if slots[i] is False:
            print(result[i], end = " ")


arr = [['a', 2, 100], # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

sequence_job(arr, 5)
