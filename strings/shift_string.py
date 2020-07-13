# program to shift strings according to given shift matrix containing direction and steps needed to shift
# 0 means shift left, 1 means right shift and first index of each row of matrix gives direction
# and second index gives steps
# since the constrains are small, so 0(n*n) can be passed here.

def reverse(s, start, end):
    l = list(s)
    while(start < end):
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1
    return "".join(l)

def left_rotate_reverse(s, k):
    print("left roatet")
    n = len(s)
    k = k % n
    s = reverse(s, 0, k-1)
    s = reverse(s, k, n-1)
    s = reverse(s, 0, n-1)
    return s

def rotate_right_reverse(s, k):
    print("right torate")
    n = len(s)
    k = k % n
    s = reverse(s, 0, n - k - 1)
    s = reverse(s, n - k, n - 1)
    s = reverse(s, 0, n - 1)
    return s

def shift_string(s, shift):
    for i in shift:
        dir, steps = i[0], i[1]
        if not dir:
            s = left_rotate_reverse(s, steps)
        else:
            s = rotate_right_reverse(s, steps)
        print(s)

    return s

# main driver function
if __name__ == '__main__':
    shift = [[0, 1], [1, 2]]
    s = "abc"
    assert shift_string(s, shift) == "cab"
