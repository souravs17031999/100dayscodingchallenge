# Program for finding the max. height of the box stacked up only if upper box has lesser base area to the
# lower box.
# We can use different rotations of the same box and use it multiple times for making the stack.
# -----------------------------------------------------------------------------------------------------------------
# Since, it seems very much similar to the LIS longest increasing subsequence problem, so we will apply the same logic.
# But firstly we need to sort on the basis of base area as if there is a box of bigger area currently relative to the already
# box taken previously, then surely it can't be at the top of previously added box in the stack.
# Hence, we sort so that each box has possibility of going up the top of previously added stack of boxes.
# Thereby, increasing/maximizing the height.
# -----------------------------------------------------------------------------------------------------------------
# Logic of sorting will make this problem easier to be seen as LIS problem.
# Let's say after sorting :
# 20 15 8 4 3 ...... (base areas)
# Now, we can easily visualize the next box to be selected only if the area is smaller than the previous box, so we
# are not sure of the current box selection but atleast it has a possibility of selection, rest our DP search will tell.
# ----------------------------------------------------------------------------------------------------------------
# Main thing is to rotate the boxes so that we can make the upper box fit into the lower boxes.
#  EX. dimensions of box  : {1x2x3}, so there can always be three atmost rotations possible generated by fixing the height one by one like below :
# {1, 2, 3}, {2, 1, 3}, {3, 1, 2} once height fixed, we don;t care about order of rest two, because we are concerned only about the base area.
# Overall, space taken will be 3*N, where N is number of boxes since for each box, there can be 3 possible atmost rotations.
# TIME: 0(N ^ 2), SPACE : 0(3*N) ~ 0(N)


# Dynamic Programming implementation
# of Box Stacking problem
class Box:

	# Representation of a box
	def __init__(self, h, w, d):
		self.h = h
		self.w = w
		self.d = d

def maxStackHeight(arr, n):

	# Create an array of all rotations of
	# given boxes. For example, for a box {1, 2, 3},
	# we consider three instances{{1, 2, 3},
	# {2, 1, 3}, {3, 1, 2}}
	rot = [Box(0, 0, 0) for _ in range(3 * n)]
	index = 0

	for i in range(n):

		# Copy the original box
		rot[index].h = arr[i].h
		rot[index].d = max(arr[i].d, arr[i].w)
		rot[index].w = min(arr[i].d, arr[i].w)
		index += 1

		# First rotation of the box
		rot[index].h = arr[i].w
		rot[index].d = max(arr[i].h, arr[i].d)
		rot[index].w = min(arr[i].h, arr[i].d)
		index += 1

		# Second rotation of the box
		rot[index].h = arr[i].d
		rot[index].d = max(arr[i].h, arr[i].w)
		rot[index].w = min(arr[i].h, arr[i].w)
		index += 1

	# Now the number of boxes is 3n
	n *= 3

	# Sort the array 'rot[]' in non-increasing
	# order of base area
	rot.sort(key = lambda x : x.w * x.d, reverse = True)

	# Uncomment following two lines to print
	# all rotations
	# for i in range(n):
	#	 print(rot[i].h, 'x', rot[i].w, 'x', rot[i].d)

	# Initialize msh values for all indexes
	# msh[i] --> Maximum possible Stack Height
	# with box i on top
	msh = [0] * n

	for i in range(n):
		msh[i] = rot[i].h

	# Compute optimized msh values
	# in bottom up manner
	for i in range(1, n):
		for j in range(0, i):
			if (rot[i].w < rot[j].w and
				rot[i].d < rot[j].d):
				if msh[i] < msh[j] + rot[i].h:
					msh[i] = msh[j] + rot[i].h

	maxm = -1
	for i in range(n):
		maxm = max(maxm, msh[i])

	return maxm

# Driver Code
if __name__ == "__main__":
	arr = [Box(4, 6, 7), Box(1, 2, 3),
		Box(4, 5, 6), Box(10, 12, 32)]
	n = len(arr)
	print("The maximum possible height of stack is",
		maxStackHeight(arr, n))
