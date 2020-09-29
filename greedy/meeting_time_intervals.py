# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# We use here greedy approach similar to activity selection problem.

# meeting time intervals = [[0, 30],[5, 10],[15, 20]]

# after sorting on finish : [[5, 10], [15, 20], [0, 30]]

def compute_meeting_room(arr):
    
    arr.sort(key = lambda x : x[1])
    for i in range(len(arr)):
        if arr[i][1] > arr[i + 1][0]:
            return False
    
    return True
    
if __name__ == '__main__':
    
    arr = [[0, 30],[5, 10],[15, 20]]
    print(compute_meeting_room(arr))
