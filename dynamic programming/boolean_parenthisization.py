# Program for computing the number of ways in which given expression evaluates to True.
# Allowed symbols are ["T" : True, "F" : False] and allowed operators are ["|" : OR, "&"  : AND, "^" : XOR]
# EX.
# expression : "T ^ F & T"
# so, symbols : [T, F, T]
# and opr :     [^, &]
# So, there are two ways such that this evaluates to True,
# "((T ^ F) & T)" and "(T ^ (F & T))"
# EX.
# expression : "T | T & F ^ T"
# so, there are 4 ways for it to be True,
# ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T))
#
# This is again a variation of MCM as we need to put brackets in order to count the total ways.
# First we need to understand the MCM format.
# Firstly, we select variables for input, that is (string, i, j), now is it sufficient? No, as it doesn't tell us about the status of the True/False
# which one needs to be evaluated.
# Actually, to count all the ways for the expression to be True, we also need to count the number of ways to be False
# for either sides as can be seen below.
#
# XOR :
# T ^ T => F
# T ^ F => T
# F ^ T => T
# F ^ F => F
# AND :
# T & T => T
# T & F => F
# F & T => F
# F & F => F
# OR :
# T | T => T
# T | F => T
# F | T => T
# F | F => F
#
# BASE CONDITIONS : if i > j: return False , if  i==j, then it depends on the fourth input(isTrue), depending on that return the valid output.
# LOOP CONDITIONS : every time, we break at k, and it will be always operator and not symbol, also every time we need to jump to +2 for valid brackets,
# so, k from i + 1, to j - 1, using +2 jumps.
# MAIN COMPUTATION : compute the ways for lT, Lf, Rt and Rf
# AND THEN DEPENDING UPON WHICH OPERATOR K IS ON, UPDATE THE COUNT USING THE ALL THE WAYS FOR IT TO BE TRUE OR FALSE (DEPENDS ON is_true).
# ---------------------------------------------------------------------------------------------------------------------------------
# OPTIMIZED TO 0(N^3) AND 0(N^2) SPACE

# simple recursion
def evaluate(s, i, j, is_true):

    if i > j:
        return False

    if i == j:
        if is_true == 'T':
            return s[i] == 'T'
        else:
            return s[i] == 'F'

    ans = 0
    for k in range(i + 1, j, 2):

        lt = evaluate(s, i, k - 1, 'T')
        lf = evaluate(s, i, k - 1, 'F')
        rt = evaluate(s, k + 1, j, 'T')
        rf = evaluate(s, k + 1, j, 'F')

        if s[k] == '&':
            if is_true == 'T':
                ans += lt * rt
            else:
                ans += lt * rf + lf * rt + lf * rf

        elif s[k] == '|':
            if is_true == 'T':
                ans += lt * rt + lt * rf + lf * rt
            else:
                ans += lf * rf
        else:
            if is_true == 'T':
                ans += lt * rf + lf * rt
            else:
                ans += lt * rt + lf * rf

    return ans

# TOP DOWN Memoization :
# Here, we have to make 3d Matrix => i * j * is_true of dp[max(i)][max(j)][2]
# But it will be too complex, so we will do it with dict whose keys (i, j, is_true) and value is computed value.

cache = {}
def evaluate_memo(s, i, j, is_true):

    if i > j:
        return False

    if i == j:
        if is_true == 'T':
            return s[i] == 'T'
        else:
            return s[i] == 'F'

    if (i, j, is_true) in cache:
        return cache[(i, j, is_true)]

    ans = 0
    for k in range(i + 1, j, 2):

        lt = evaluate_memo(s, i, k - 1, 'T')
        lf = evaluate_memo(s, i, k - 1, 'F')
        rt = evaluate_memo(s, k + 1, j, 'T')
        rf = evaluate_memo(s, k + 1, j, 'F')

        if s[k] == '&':
            if is_true == 'T':
                ans += lt * rt
            else:
                ans += lt * rf + lf * rt + lf * rf

        elif s[k] == '|':
            if is_true == 'T':
                ans += lt * rt + lt * rf + lf * rt
            else:
                ans += lf * rf
        else:
            if is_true == 'T':
                ans += lt * rf + lf * rt
            else:
                ans += lt * rt + lf * rf

    cache[(i, j, is_true)] = ans
    return ans



# BOTTOM UP DP :
# Returns count of all possible
# parenthesizations that lead to
# result true for a boolean
# expression with symbols like
# true and false and operators
# like &, | and ^ filled between symbols
def countParenth(symb, oper, n):
	F = [[0 for i in range(n + 1)]
			for i in range(n + 1)]
	T = [[0 for i in range(n + 1)]
			for i in range(n + 1)]

	# Fill diaginal entries first
	# All diagonal entries in
	# T[i][i] are 1 if symbol[i]
	# is T (true). Similarly, all
	# F[i][i] entries are 1 if
	# symbol[i] is F (False)
	for i in range(n):
		if symb[i] == 'F':
			F[i][i] = 1
		else:
			F[i][i] = 0

		if symb[i] == 'T':
			T[i][i] = 1
		else:
			T[i][i] = 0

	# Now fill T[i][i+1], T[i][i+2],
	# T[i][i+3]... in order And
	# F[i][i+1], F[i][i+2],
	# F[i][i+3]... in order
	for gap in range(1, n):
		i = 0
		for j in range(gap, n):
			T[i][j] = F[i][j] = 0
			for g in range(gap):

				# Find place of parenthesization
				# using current value of gap
				k = i + g

				# Store Total[i][k] and Total[k+1][j]
				tik = T[i][k] + F[i][k];
				tkj = T[k + 1][j] + F[k + 1][j];

				# Follow the recursive formulas
				# according to the current operator
				if oper[k] == '&':
					T[i][j] += T[i][k] * T[k + 1][j]
					F[i][j] += (tik * tkj - T[i][k] *
											T[k + 1][j])
				if oper[k] == '|':
					F[i][j] += F[i][k] * F[k + 1][j]
					T[i][j] += (tik * tkj - F[i][k] *
											F[k + 1][j])
				if oper[k]=='^':
					T[i][j] += (F[i][k] * T[k + 1][j] +
								T[i][k] * F[k + 1][j])
					F[i][j] += (T[i][k] * T[k + 1][j] +
								F[i][k] * F[k + 1][j])
			i += 1
	return T[0][n - 1]

# Driver Code
symbols = "TTFT"
operators = "|&^"
n = len(symbols)

# There are 4 ways
# ((T|T)&(F^T)), (T|(T&(F^T))),
# (((T|T)&F)^T) and (T|((T&F)^T))
print(countParenth(symbols, operators, n))



if __name__ == '__main__':
    print(evaluate("T^F&T", 0, len("T^F&T") - 1, 'T'))
    print(evaluate("T^F|F", 0, len("T^F|F") - 1, 'T'))
    print(evaluate("T|T&F^T", 0, len("T|T&F^T") - 1, 'T'))
    print(evaluate_memo("T^F&T", 0, len("T^F&T") - 1, 'T'))
    print(evaluate_memo("T^F|F", 0, len("T^F|F") - 1, 'T'))
    print(evaluate_memo("T|T&F^T", 0, len("T|T&F^T") - 1, 'T'))
