# Program for candy distribution problem.
# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Example 1:
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.

# -----------------------------------------------------------------------------------------------------------------

# TIME : 0(N), SPACE : 0(N)
# Using two arrays
class Solution:
    def candy(self, ratings: List[int]) -> int:

        candy_left = [1] * len(ratings)
        candy_right = [1] * len(ratings)

        if not ratings:
            return 0

        n = len(ratings)

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy_left[i] = candy_left[i - 1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy_right[i] = candy_right[i + 1] + 1

        res = 0
        for i in range(n):
            res += max(candy_left[i], candy_right[i])

        return res

# Using only one extra array :
class Solution:
    def candy(self, ratings: List[int]) -> int:

        candy = [1] * len(ratings)

        if not ratings:
            return 0

        n = len(ratings)

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)


        return sum(candy)

# single pass, constant space 
