# heap's algorithm to find all the permutations of the given array / string .
# At each step, on k initial elements of the collection.
# Initially k == n, and thereafter k  < n, each step generates k! permutations that end with same
# n - k final elements.
# It does this by calling itself once with the kth element unaltered and then k - 1 times with the
# kth element exchanged for each of the initial k - 1 final elements.
# The recursive calls modify the initial k - 1 elements and a rule is needed at each iteration
# to select which will be exchanged with the last.
# This is done by parity of the number of elements operated on at this step, if k is even,
# final element is iteratively exchanged with each element index.
# if k is odd, then final element is always exchanged with the first.
# TIME : 0(N!) since N! permutations in all ,
# SPACE : 0(N) , each permutation requires amortised 0(1) time.

def printArr(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
    print()

def heapPermutations(arr, size, n):
    if size == 1:
        printArr(arr, n)
        return

    for i in range(size):
        heapPermutations(arr, size - 1, n)

        if size & 1:
            arr[0], arr[size - 1] = arr[size - 1], arr[0]
        else:
            arr[i], arr[size - 1] = arr[size - 1], arr[i]

if __name__ == '__main__':
    arr = [1, 2, 3]
    n = len(arr)
    heapPermutations(arr, n, n)
