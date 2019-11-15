# program to implement counting sort algorithm for both positive and negative arrays

# IDEA: logic is to use a temporary array for storing the count / occurence of every integer in the list , now items are sorted index wise and then
# we simply loop that many times the value is at that index and put that index value in the original array that many times (in-place only for moving elements back in sorted but then also we are using extra space 0(k) auxiliary space for storing counts.)
from sys import stdin, stdout

def counting_sort(arr, n):
    # we make array of maximum length so that biggest integer (element) is accomodated
    k = max(arr) + 1
    # intializing the list with 0's
    count = [0] * k
    # storing the count of each element by incrementing the default value of 0
    for i in range(n):
        count[arr[i]] += 1
    # keeping a pointer to original array
    j = 0
    # looping over count array
    for i in range(k):
        temp = count[i]
        # loop that many times as there is value so that it is consecutive (including duplicacy)
        while(temp):
            arr[j] = i
            temp -= 1
            j += 1
    return arr

# main function 
if __name__ == '__main__':
    arr = list(map(int, stdin.readline().strip().split()))
    n = len(arr)
    print(counting_sort(arr, n))
