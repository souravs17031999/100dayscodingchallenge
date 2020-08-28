# Program for computing minimum and maximum value for the expression.
# EX.                [1+2*3+4*5]
#                        /  \
#      [1 + (2*3) + (4*5)]  [(1 + 2) * (3 + 4) * 5]
#           min = [27]         max = [105]
#
# So, we need to actually put brackets in such a order to get min as well as some ordering in which we get max value.
# Then, there are two operators here as we can see => "+" and "*"
# so, this is variation of MCM.
# Now, since we have two operators here, we will create a new array for separately numbers and then for operators.
# Then, depending on operators we will apply the operations as required and update the min and max value both.
# Here, we also require 2 , 2d dp arrays, where dp[i][j] state reperesents, the minvalue and maxvalue for index i...j
# Now, we will break this into subproblems with the help of k, from i....k and k+1....j
# -------------------------------------------------------------------------------------------------------------------
# Python3 program to get maximum and minimum
# values of an expression

# Utility method to check whether a character
# is operator or not
def isOperator(op):
	return (op == '+' or op == '*')

# method prints minimum and maximum value
# obtainable from an expression
def printMinAndMaxValueOfExp(exp):
	num = []
	opr = []
	tmp = ""

	# store operator and numbers in different vectors
	for i in range(len(exp)):
		if (isOperator(exp[i])):
			opr.append(exp[i])
			num.append(int(tmp))
			tmp = ""
		else:
			tmp += exp[i]

	# storing last number in vector
	num.append(int(tmp))

	llen = len(num)
	minVal = [[ 0 for i in range(llen)] for i in range(llen)]
	maxVal = [[ 0 for i in range(llen)] for i in range(llen)]

	# initializing minval and maxval 2D array
	for i in range(llen):
		for j in range(llen):
			minVal[i][j] = 10**9
			maxVal[i][j] = 0

			# initializing main diagonal by num values
			if (i == j):
				minVal[i][j] = maxVal[i][j] = num[i]

	# looping similar to matrix chain multiplication
	# and updating both 2D arrays
	for L in range(2, llen + 1):
		for i in range(llen - L + 1):
			j = i + L - 1
			for k in range(i, j):

				minTmp = 0
				maxTmp = 0

				# if current operator is '+', updating tmp
				# variable by addition
				if(opr[k] == '+'):

					minTmp = minVal[i][k] + minVal[k + 1][j]
					maxTmp = maxVal[i][k] + maxVal[k + 1][j]


				# if current operator is '*', updating tmp
				# variable by multiplication
				elif(opr[k] == '*'):

					minTmp = minVal[i][k] * minVal[k + 1][j]
					maxTmp = maxVal[i][k] * maxVal[k + 1][j]

				# updating array values by tmp variables
				if (minTmp < minVal[i][j]):
					minVal[i][j] = minTmp
				if (maxTmp > maxVal[i][j]):
					maxVal[i][j] = maxTmp

	# last element of first row will store the result
	print("Minimum value : ",minVal[0][llen - 1],", \
			Maximum value : ",maxVal[0][llen - 1])

# Driver code
expression = "1+2*3+4*5"
printMinAndMaxValueOfExp(expression)
