# Program to sort the tuples given first in the order of their second index values.
# Then, sort lexographically according to first index.
# Ex. First index in the tuple here contains "names", second index in the tuple
# here contains "values(salaries)".

def sort_string(arr, n, x):
    arr.sort(key = lambda x : (x[1], x[0]), reverse = True)
    print(arr)

if __name__ == '__main__':
    arr = [['Eve', 78], ['Bob', 99], ['Suzy', 86], ['Alice', 86]]
    n = len(arr)
    x = 79
    sort_string(arr, n, x)
