# Program to compute the kth permutation for a given N and K.
# Input: n = 3, k = 3
# Output: "213"
# Input: n = 4, k = 9
# Output: "2314"
# -------------------------------------------------------------------------------------------------------------------------------------
# Observations :
# [1, 2, 3] =>
# [1, 2, 3], [1, 3, 2], | [2, 1, 3], [2, 3, 1], | [3, 1, 2], [3, 2, 1]
# [1, 2, 3, 4] =>
# [1, 2, 3, 4] => [1234], [1243], [1324], [1342], [1423], [1432] | [2134], [2143], [2314], [2341] ..... | [3, ....] ... | [4 ,.....].....
# So, as we see from above two examples , that these permutations can be divided into buckets based on the same items on signifcant digits.
# As we also see, first digit changes after 6 permutations (n - 1)!, similarly second digit changes after 2 permutations (n - 2)! and so on...

# Now, how do we get the buckets in which kth permutation lie ?
# it is given by k / (n - 1) !
# Now, we first get the bucket and fix the first char of the given string or array, then, we erase that char from our string/array and then
# go for second signifcant digit, that is to fix the second char after fixing the first char.
# Factorials value can be very large so we precompute it in order to avoid computing Factorials again.
# Then, we create a temp new array => [1.....N], and so we can now have a array for all numbers from 1, 2, 3, ....N
# We start from N, K and recurse for smaller subproblems N-1, K and maintain a ans variable which appends the char one by one after fixing the char.
# --------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factor = factorial(n-1)
        k -= 1 # index starts from 1 in the question but our list indexs starts from 0
        ans = []
        numbers_left = list(range(1,n+1))

        for m in range(n-1,0,-1):
            index = int(k // factor)
            ans += str(numbers_left[index])
            numbers_left.pop(index)
            k %= factor
            factor /= m

        ans += str(numbers_left[0])
        return ''.join(ans)

# ----------------------------------------------------------------------------------------------------------------------------------------------
# TIP : DON'T USE STRING FOR MODIFCATIONS, RATHER USE LIST AND THEN FINALLY JOIN.

if __name__ == '__main__':
    N, K = 3, 5
    compute_Kth(N, K)
