# 1. Program for computing required rooms for conducting meetings such that no two meetings overlap over each other and also each room can conduct only one meeting at a time.

# meeting time intervals = [[0, 30],[5, 10],[15, 20]]

# after sorting on finish : [[5, 10], [15, 20], [0, 30]]

# => [0, 5, 15]
# => [10, 20, 30]

# rooms = 2

# TIME : 0(N* Log(N)), SPACE : 0(N)

def compute_conf_room(arr):
    
    start = [x[0] for x in arr]
    end = [x[1] for x in arr]
    
    start.sort()
    end.sort()
    rooms, end_i = 0, 0
    for i in range(len(arr)):
        if start[i] < end[end_i]:
            rooms += 1
        else:
            end_i += 1
    
    return rooms
    
# # 2. Program for computing if given number of queries can be accomodated in the given calendar days and given number of rooms.
# Input: calendar = [[1, 2], [4, 5], [8, 10]], rooms = 1, queries = [[2, 3], [3, 4]]
# Output: [true, true]

calendar = [[1, 2], [4, 5], [8, 10]]
res = [None] * len(calendar)
for i in range(len(calendar)):
    calendar.append(queries[i])
    if compute_conf_room(arr) <= rooms:
        res[i] = True
    calendar.remove(len(calendar) - 1)

 return res
    
    
if __name__ == '__main__':
    
    arr = [[0, 30],[5, 10],[15, 20]]
    print(compute_conf_room(arr))
