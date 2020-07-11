# Program for activity selection problem -> Given a set of (i, j) activities in a 2-d matrix where i denotes start times,
# and j denotes finish times.
# We need to be able to find the maximum activity a person can do given atmost he can do only one activity at a time.
# IDEA: Logic is to use Greedy approach as can be approached, if we go by local optimal, we are probable of approaching global
# optimal solutions.
# So, we firstly sort all the finish times, and then greedy selection is to pick those finish times which are earliest and also
# whose start times are greater than finish times.
# In this way, we can maintain a count of activities possible, and also print the activity (if asked).
# NOTE : First activity is always selected to be clear, and mathematically proven to be always optimal.
# TIME :  0(N*lg(N)), SPACE : Not constant (due to tim sort) [we can apply here Counting sort due to involvement of integers and reduce
# the complexity to 0(N)]

from sys import stdin, stdout

def selectActivity(arr, n):
    # sort the array acc. to finish times
    arr.sort(key = lambda x : x[1])
    count = 1
    i = 0 # i basically identifies the activities that are already selected, so first is already selected.
    for j in range(1, n):
        # now for other items (activities), we select those which have start time greater than finish times.
        if arr[j][0] >= arr[i][1]:
            count += 1
            i = j
    return count


# driver test function
if __name__ == '__main__':
    test = int(stdin.readline().strip())
    while test:
        arr = []
        n = int(stdin.readline().strip())
        for i in range(n):
            arr.append(list(map(int, stdin.readline().strip().split())))
        selectActivity(arr, n)
        test -= 1
