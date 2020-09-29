
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
    
if __name__ == '__main__':
    
    arr = [[0, 30],[5, 10],[15, 20]]
    print(compute_conf_room(arr))
