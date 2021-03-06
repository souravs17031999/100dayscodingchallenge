# Program to find next greater permutation lexographically, and if it is not possible, then
# then simply return the sorted order in ascending form.
# IDEA: Logic is to first know some facts :
#--------
# * If the array is in descending order, then there is no next permutation possible, as it is the last greater permutation.
# * Now, if the array is already in descending order, then reversal of it will produce array in ascending order.
#---------
# Logic is to find first element pointer "i" at which index, (right->left) that element will be smaller than the just after the element.
# because we have assumed array to be descending to it the last , so we are tending it towards it.
# So, we need to know where this propert voilates, and then "i" points to that first element.
# Like in some permutation : [1, 3, 5, 4, 2] => break point is 3 (index=1).

# Then, we find first closer greater element (right->left), pointed at by "j".
# Because we need lexpgraphically next greater element, so, we need the closest greater element that is 4, index(= 3).

# We swap both of those to produce next permutation => [1, 4, 5, 3, 2]

# Now, we also reverse the array after the pointer "i" till last element, in order to make it lexigraphically (sorted order)
# to get the lowest rank possible in order to further
# generate next permutations.

# Intution for reversing ?
# --------------------------------------------------------------------------------------------------------------------------------------------------
# Intution behind reverse is that after swapping the i, j element, we have produced last permutation as descending section is there still,
# so, we simply reverse to make it ascending section to get the lowest rank possible first.
# EX. [1, 2, 3] => firstly we swap 2, 3 and then get [1, 3, 2] => then, we reverse after 2, that is no change.
# Now, we simply swap 1, 2 => [2, 3, 1], if we observe then we will see that this is greatest permutation possible for the descending order seciton, and
# so, we need to reverse it to get, reverse after 2, to get [2, 1, 3] (this is correct third permutation)
# Then, we need to swap 1, 3 => [2, 3, 1] and now, we swap 2, 3 => [3, 2, 1] and again now if we don't reverse then we will directly jumpt to [1, 2, 3]
# which is wrong totally, because then total we would have 5 permutation but we know we have 6 permutation, so we first reverse it => [3, 1, 2]
# to get lower rank permutation first, now we again swap, 1, 2 = > [3, 2, 1] and reverse after 2 which does nothing = >
# [3, 2, 1] (this is last permutation)
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# [1, 4, 2, 3, 5] => will give us the exact next permutation.

# If at any point, "i" becomes -ve, that means the array is already sorted in descending order, hence we simply reverse it to
# return the ascending array sorted order as there is no more next permutation possible for it.
# TIME : 0(N), SPACE : 0(1).

# function to reverse in-place
def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

# function to generate next permutation
def next_permutation(arr, n):
    # i points to first element where descending property is voilated.
    i = n - 2
    while i >=0 and arr[i] >= arr[i + 1]:
        i -= 1

    # j points to first closer greater element
    j = n - 1
    while j >=0 and arr[j] <= arr[i]:
        j -= 1

    if i < 0:
        # it means array is sorted in descending order, so we simply reverse it.
        reverse(arr, 0, n - 1)
        return

    # otherwise, simply swap i, j
    arr[i], arr[j] = arr[j], arr[i]
    # reverse from after i + 1 to produce lexographic order so that first of these permutations comes first.
    reverse(arr, i + 1, n - 1)

# driver test function
if __name__ == '__main__':
    arr = [4, 5, 6, 3, 2, 1]
    n = 6
    print(arr)
    next_permutation(arr, n)
    print(arr)
