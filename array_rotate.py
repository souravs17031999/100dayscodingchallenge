def reverse(l, start, end):
    while(start < end):
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1

def reverse_rotate(l, k):
    n = len(l)
    reverse(l, 0, k-1)
    reverse(l, k, n-1)
    reverse(l, 0, n-1)
    print(l)

def left_rotate_temp(l, k):
    temp = []
    n = len(l)
    for i in range(0, k):
        temp.append(l[i])
    j = 0
    for i in range(k, n):
        l[j] = l[i]
        j += 1
    j = 0
    for i in range(n - k, n):
        l[i] = temp[j]
        j += 1
    print(l)

def main_rotate(l, k):
    l1 = l.copy()
    print(f"Original list: {l}")
    print("Modified list after rotation using temp array :")
    left_rotate_temp(l, k)
    print(f"Modified list after using reverse rotate : ")
    reverse_rotate(l1, k)

if __name__ == "__main__":
    print("Give the elements of the original list followed by number of rotations : ")
    u_input = list(map(int, input().strip().split()))
    r_input = int(input().strip())
    main_rotate(u_input, r_input)
