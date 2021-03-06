# program for rotating array by k times using two methods

# First method using reversal algorithm
def reverse(l, start, end):
    '''
    parameters :
    l - list of elements
    start - start index (leftmost)
    end - end index (rightmost)

    '''
    while(start < end):
        l[start], l[end] = l[end], l[start]  # swapping start index element with last  element index till start coincides with end
        start += 1
        end -= 1

def left_rotate_reverse(l, k):
    '''
    parameters :
    l - list of elements
    k - number by which array is rotated

    '''
    n = len(l)
    k = k % n  # if k goes out of range of list, then wrap it inside the range
    reverse(l, 0, k-1)  # reverse first half of array
    reverse(l, k, n-1)  # reverse last half of array
    reverse(l, 0, n-1)  # reverse overall array
    print(l)


'''
# second method using temporary array
def left_rotate_temp(l, k):

    parameters :
    l - list of elements
    k - number by which array is rotated


    temp = []
    n = len(l)
    # first we shift all k elements in a temporary array
    for i in range(0, k):
        temp.append(l[i])
    j = 0
    # then shift the remaning element one by one
    for i in range(k, n):
        l[j] = l[i]
        j += 1
    j = 0
    # shift back all the elements from temporary to main array
    for i in range(n - k, n):
        l[i] = temp[j]
        j += 1
    print(l)
'''
'''
# for right rotation , reversing from back side


def rotate_right_reverse(l, k):
	setting the pivot point from back side 
    n = len(l)
    k = k % n
    reverse(l, 0, n - k - 1)
    reverse(l, n - k, n - 1)
    reverse(l, 0, n - 1)
    print(l)


'''
def main_rotate(l, k):
    '''
    parameters :
    l - list of elements
    k - number by which array is rotated

    '''
    print(f"Original list: {l}")
    print(f"Modified list rotate : ")
    left_rotate_reverse(l, k)

if __name__ == "__main__":
    print("Give the elements of the original list followed by number of rotations : ")
    u_input = list(map(int, input().strip().split()))
    r_input = int(input().strip())
    main_rotate(u_input, r_input)
