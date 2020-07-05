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

    # Note  : Counting sort for Negative numbers
    # idea is to store counts but for postive numbers only by mapping negative numbers to their positive counterparts by taking how much far my number is
    # from minimum number, as minimum will be -ve and so we can get positive indices by subracting -ve numbers.
    # and then when we need to get back our original numbers, we again add up the min and current element.
    def counting_sort_neg(arr, n):
        min_ele = min(arr)
        size_range = max(arr) - min(arr) + 1
        count = [0 for _ in range(size_range)]
        # calculating counterpart of this negative number to map to its positive index
        for i in range(len(arr)):
            count[arr[i] - min_ele] += 1

        j = 0
        for i in range(size_range):
            temp = count[i]
            while temp:
                arr[j] = i + min_ele # use -(i + min_ele) for descending order
                temp -= 1
                j += 1

        print(arr)

    # idea is to compute first simply compute frequencies, then prefix sum, then we need to again find the position for the original array
    def main_counting_sort(arr, n):
        k = max(arr) + 1
        # output for sorted array
        output = [0 for _ in range(len(arr))]
        # count storage , auxiliary array
        count = [0 for _ in range(k)]
        # compute frequecnies
        for i in range(len(arr)):
            count[arr[i]] += 1
        # compute prefix sum
        for i in range(1, k):
            count[i] += count[i - 1]
        # finally, placing input elements in their correct positions , going from back to produce stable sort ,
        # otherwise traversing from front will also work but not stable
        for i in range(len(arr)-1, -1, -1):
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1

        print(output)

# main function
if __name__ == '__main__':
    arr = list(map(int, stdin.readline().strip().split()))
    n = len(arr)
    print(counting_sort(arr, n))
    input_list = [random.randint(-10000, 10000) for _ in range(10000)]
    counting_sort_neg(input_list, len(input_list))
