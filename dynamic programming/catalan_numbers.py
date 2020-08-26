# Program for computing catalan numbers for upto n (can also be used to compute nth catalan number)
# Catalan numbers are sequence of natural numbers defined recursively :
# C0 = 1 and C0(i + 1) = sigma(C(i), C(i-1)) from i from 0 to n
# To compute nth catalan number, we need to return catalan[n] as we are storing all catalan numbers till n - 1.
# Time  : 0(N^2), SPACE : 0(N)
# -------------------------------------------------------------------------------------------------------
# APPLICATIONS :
# * 1, 1, 2, 5, 14, 42, 132,............
# * Cn is the number of Dyck words of length 2n. A Dyck word is a string consisting of n X's and n Y's such that no
# initial segment of the string has more Y's than X's. For example, the following are the Dyck words of length 6: XXXYYY XYXXYY XYXYXY XXYYXY XXYXYY
# * Re-interpreting the symbol X as an open parenthesis and Y as a close parenthesis, Cn counts the number of expressions containing n pairs of parentheses which are correctly matched:
# ((()))     ()(())     ()()()     (())()     (()())
# * Cn is the number of different ways n + 1 factors can be completely parenthesized (or the number of ways of associating n applications of a binary operator). For n = 3,
# for example, we have the following five different parenthesizations of four factors:
# ((ab)c)d     (a(bc))d     (ab)(cd)     a((bc)d)     a(b(cd))
# * Successive applications of a binary operator can be represented in terms of a full binary tree.
# (A rooted binary tree is full if every vertex has either two children or no children.) It follows that Cn is the number of full binary trees with n + 1 leaves:
# * Cn is the number of non-isomorphic ordered trees with n + 1 vertices. (An ordered tree is a rooted tree in which the children of each vertex are given a fixed left-to-right order.)
# * Cn is the number of ways to form a "mountain range" with n upstrokes and n downstrokes that all stay above a horizontal line.
# The mountain range interpretation is that the mountains will never go below the horizon.
# * A convex polygon with n + 2 sides can be cut into triangles by connecting vertices with non-crossing line segments (a form of polygon triangulation).
# The number of triangles formed is n and the number of different ways that this can be achieved is Cn
# Cn is the number of monotonic lattice paths along the edges of a grid with n × n square cells, which do not pass above the diagonal.
# A monotonic path is one which starts in the lower left corner, finishes in the upper right corner, and consists entirely of edges pointing rightwards or upwards.
# Counting such paths is equivalent to counting Dyck words: X stands for "move right" and Y stands for "move up".
# In chemical engineering Cn−1 is the number of possible separation sequences which can separate a mixture of n components.[8]

# -------------------------------------------------------------------------------------------------------

def catalan(n):

    catalan = [0 for _ in range(n + 1)]
    catalan[0] = catalan[1] = 1
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    return catalan

# more optimized version to compute just the nth catalan number in 0(N) time and 0(1) space.

# function to return the binomal coefficent of n C k
def binom(n, k):
    # if k is greater than n that means , c(n, k) = c(n, n - k) using properties of binomial , helps to reduce calculation
    if k > n - k:
        k = n - k
    # initializing result
    res = 1
    for i in range(k):
        # calculating numerator part
        res *= n - i
        # calculating denominator part
        res /= i + 1
    return int(res)

# function to get nth catalan numbers
def catalan_binom(n):
    c = binom(2*n, n)
    return c // (n + 1)

# main function
if __name__ == '__main__':
    print(catalan(10))
