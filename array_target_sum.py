# Program for finding all unqiue pairs for which sums up to some target value in a array
def binary_search(l, start, end, key):
    while(start <= end):
        middle = start + (end - start) // 2
        if key < l[middle]:
            end = middle - 1
        elif key > l[middle]:
            start = middle + 1
        else:
            return 1
    return 0

def array_target_sum_main(l, target):
    l.sort()
    n = len(l)
    a = []
    for i in range(len(l)):
        if l[i] > 0:
            result = target - l[i]
        else:
            result = l[i] - target
        if l[i] != result:
            if(binary_search(l, 0, n, result)):
                if l[i] not in a or result not in a:
                    print("{} and {}".format(l[i], result))
                    a.append(l[i])
                    a.append(result)


n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
target = int(input())
array_target_sum_main(l, target)
