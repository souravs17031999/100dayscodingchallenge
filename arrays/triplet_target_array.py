# program to find triplet of numbers which add up to some target sum for a given array

# function to find the triplet and print the triplet
# idea is to first sort the array, then fix one of the element and then choose/select other two required like the same finding pair for a sum problem
def triple_sum(l, target):
    # sort the array
    l.sort()
    # fixing one element one by one
    for i in range(len(l)-2):
        if i>0 and l[i]==l[i-1]: continue
        # setting first index as always the next one of choosen element
        start = i + 1
        end = len(l) - 1
        # now we know the target for a pair to be find
        k = target - l[i]
        # finding those other two for the fixed element
        while(start < end):
            if l[start] + l[end] == k:
                print(f'{l[i]}, {l[start]} and {l[end]}')
                # if removing duplicates, then
                while start < end and l[start] == l[start - 1]: start += 1
                while start < end and l[end] == l[end + 1]: end -= 1
                start += 1
                end -= 1
            if l[start] + l[end] > k:
                end -= 1
            else:
                start += 1

# main function
if __name__ == '__main__':
    t = int(input().strip())
    l = []
    for i in range(t):
        l.append(int(input().strip()))
    target = int(input().strip())
    triple_sum(l, target)
