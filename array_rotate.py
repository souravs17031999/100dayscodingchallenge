# Program for finding all unqiue pairs for which sums up to some target value in a array

def array_target_sum_main(l, target):
    l.sort()
    start = 0
    end = len(l) - 1
    while(start < end):
        if(l[start] + l[end] == target):
            print(f"{l[start]} and {l[end]}")
        if(l[start] + l[end] > target):
            end -= 1
        else:
            start += 1


n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
target = int(input())
array_target_sum_main(l, target)
