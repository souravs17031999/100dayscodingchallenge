# program to shuffle the list, generating a random permutation of the list using fisher yates algorithm
# the logic is to simply randomly select a index from i to last element where i will vary from 0 to length of list,
# and swap that with the current element , so all in-place swapping based on random index chosen from remaining list every time.
# time : 0(N)
# space : 0(1)
import random
def shuffle(l):
    if len(l) == 0:
        return []
    if len(l) = 1:
        return [l[0]]    
    for i in range(len(l)):
        random_ele = random.randint(i, len(l)-1)
        l[i], l[random_ele] = l[random_ele], l[i]
    return l

if __name__ == '__main__':
    l = [20, 4, 9, 0, 1, 11, 5, 30, 2, 15]
    print(shuffle(l))
