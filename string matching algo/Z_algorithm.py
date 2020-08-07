# Python3 program that implements Z algorithm
# Idea is based on KMP algorithm but more efficent.
# ----------------------------------------------------------------------------
# This algorithm basically precomputes called as "Z-values" in a array.
# This array values basically tells us that every value indicates that is the longest substring matching
# starting from that index where we check that value.
# Now, the important trick is that, we actualy compute this z array for the string made by concatenating
# the original string and pattern string and grouped using a special symbol separating them "$".
# Hence, overall string for which this z-array is calculated : Pattern+'$'+Text.
# After calculating the z array, we traverse the entire array and if at anytime we encounter value equal to
# length of pattern, then it means we found the pattern in the string (Text).
# And finding the index of occurence : would be idx where this value is found - len(pattern) - 1.
# ------------------------------------------------------------------------------
# The main trick is in computing this Z-array in linear time.
# -----------------------------------------------------------------------------
# Let's see the example for Z -array :
#  a b a $ a b a b
# [0 0 1 0 3 0 2 0]
# As can be seen, at every index, like index "4" is value 3, starting from there 3 is longest matching "abc".
# This is a good trick which we apply after concatenating Text and pattern into a single string and apply
# this algorithm and computes all z array values.
# ----------------------------------------------------------------------------
# TIME : 0(M + N), M, N IS LENGTH OF TEXT AND PATTERN RESPECTIVELY.
# SPACE : 0(M + N)
# -----------------------------------------------------------------------------

# Fills Z array for given string str[]
def getZarr(string, z):
	n = len(string)

	# [L,R] make a window which matches
	# with prefix of s
	l, r, k = 0, 0, 0
	for i in range(1, n):

		# if i>R nothing matches so we will calculate.
		# Z[i] using naive way.
		if i > r:
			l, r = i, i

			# R-L = 0 in starting, so it will start
			# checking from 0'th index. For example,
			# for "ababab" and i = 1, the value of R
			# remains 0 and Z[i] becomes 0. For string
			# "aaaaaa" and i = 1, Z[i] and R become 5
			while r < n and string[r - l] == string[r]:
				r += 1
			z[i] = r - l
			r -= 1
		else:

			# k = i-L so k corresponds to number which
			# matches in [L,R] interval.
			k = i - l

			# if Z[k] is less than remaining interval
			# then Z[i] will be equal to Z[k].
			# For example, str = "ababab", i = 3, R = 5
			# and L = 2
			if z[k] < r - i + 1:
				z[i] = z[k]

			# For example str = "aaaaaa" and i = 2,
			# R is 5, L is 0
			else:

				# else start from R and check manually
				l = i
				while r < n and string[r - l] == string[r]:
					r += 1
				z[i] = r - l
				r -= 1

# prints all occurrences of pattern
# in text using Z algo
def search(text, pattern):

	# Create concatenated string "P$T"
	concat = pattern + "$" + text
	l = len(concat)

	# Construct Z array
	z = [0] * l
	getZarr(concat, z)

	# now looping through Z array for matching condition
	for i in range(l):

		# if Z[i] (matched region) is equal to pattern
		# length we got the pattern
		if z[i] == len(pattern):
			print("Pattern found at index",
					i - len(pattern) - 1)

# Driver Code
if __name__ == "__main__":
	text = "GEEKS FOR GEEKS"
	pattern = "GEEK"
	search(text, pattern)
