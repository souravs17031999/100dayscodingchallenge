# Program for subsequence generation using recursion
# Although this method is inefficient, as TIME : 0(2^n), exponential time.
# Good practice for leap of faith !

def allSubsequences(arr, index, out):
    if index == len(arr):
        print(out)
    else:
        # exluding the element
        allSubsequences(arr, index + 1, out)
        # including the element
        allSubsequences(arr, index + 1, out + [arr[index]])


if __name__ == '__main__':
    arr = [1, 2, 3]
    out = []
    allSubsequences(arr, 0, out)
