# Program for range query sqrt decomposition algorithm.
# So, in questions containing range queries for problems like counting disinct elements, and other frequency based computations
# segment trees are not much helpful, so here comes MO's algorithm which is just a simple idea for processing each queries.
# This is an offline algorith, since it requires that we already know all the queries.
# ------------------------------------------------------------------------------------------------------------------------
# Idea is to keep two pointers currL, currR (which defines our current position) and L, R(which defines given range query)
# and adjust all the two pointers based on the query given to us.
# Now, preprocessing is done to ensure the optimal compexity and that is to sort the queries based on block number and then
# if same ties, then based on R.
# -----------------------------------------------------------------------------------------------------------------------------
# Python program to compute sum of ranges for different range queries

# TEMPLATE FOR SQRT decomposition:

add(position):
  count[array[position]]++
  if count[array[position]] == 3:
    answer++

remove(position):
  count[array[position]]--
  if count[array[position]] == 2:
    answer--

currentL = 0
currentR = 0
answer = 0
count[] = 0
for each query:
  // currentL should go to L, currentR should go to R
  while currentL &amp;lt; L:
    remove(currentL)
    currentL++
  while currentL &amp;gt; L:
    add(currentL)
    currentL--
  while currentR &amp;lt; R:
    add(currentR)
    currentR++
  while currentR &amp;gt; R:
    remove(currentR)
    currentR--
  output answer

# ----------------------------------------------------------------------------------------------------------------------------------------
import math

# Function that accepts array and list of queries and print sum of each query
def queryResults(arr,Q):

	#Q.sort(): # Sort by L
	#sort all queries so that all queries in the increasing order of R values .
	Q.sort(key=lambda x: x[1])

	# Initialize current L, current R and current sum
	currL,currR,currSum = 0,0,0

	# Traverse through all queries
	for i in range(len(Q)):
		L,R = Q[i] # L and R values of current range

		# Remove extra elements from previous range
		# if previous range is [0, 3] and current
		# range is [2, 5], then a[0] and a[1] are subtracted
		while currL<L:
			currSum-=arr[currL]
			currL+=1

		# Add elements of current range
		while currL>L:
			currSum+=arr[currL-1]
			currL-=1
		while currR<=R:
			currSum+=arr[currR]
			currR+=1

		# Remove elements of previous range
		# when previous range is [0, 10] and current range
		# is [3, 8], then a[9] and a[10] are subtracted
		while currR>R+1:
			currSum-=arr[currR-1]
			currR-=1

		# Print the sum of current range
		print("Sum of",Q[i],"is",currSum)

arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]
queryResults(arr,Q)
#This code is contributed by Shivam Singh
