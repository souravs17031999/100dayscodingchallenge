# Program for computing H-index of researcher.
# Researcher publishes several papers in his career and H-index is defined as some value 'h'
# such that h of the N papers citated has atleast h citations each and other remaining should
# not have more than h citations each.

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
#              received 3, 0, 6, 1, 5 citations respectively.
#              Since the researcher has 3 papers with at least 3 citations each and the remaining
#              two with no more than 3 citations each, her h-index is 3.

# There maybe possible several possible values of h-index, but we need to find max of them.

# -------------------------------------------------------------------------------------------------
# We use sorting here first, so that it gives us information about the fulfilling of above constraint
# that h value is such that h papers should have atleast h citations each.
# So, after sorting, we can say that each value should indicate in increasing value, if we found
# a value such that number of papers after that value is equal to itself, then it maybe
# a possible h-index, but we need to get max of them.
# So, we have already sorted, we can apply binary search to find that h value and can get all
# h papers such that each are greater in citations than h value by computing n - mid, where mid is
# computed while binary search.
# There is one more case when we don't have a valid h index, such that there is some value which
# doesn't equal to any valid number of elements right of it.
# So, what do we return when we don't find value ?
# Actually, in that case, our start will be crossing end pointer, and hence, simply N - start, this
# count will be valid h-index, because only that many are remaining elements and that are guaranteed
# to be greater as already sorted.


# TIME : N*LOG(N)

class Solution:

    # LOG(N)
    def find_idx(self, start, end, n, citations):

        while start <= end:
            mid = (start + end) // 2
            if citations[mid] == (n - mid):
                return citations[mid]

            elif citations[mid] > (n - mid):
                end = mid - 1
            else:
                start = mid + 1

        return n - start

    # N*LOG(N)
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        return self.find_idx(0, n - 1, n, citations)
