# program for finding ugly numbers.
# NOTE : ugly numbers are those numbers whose only prime factors are from {2, 3, 5}.
# --------------------------------------------------------------------------------------------
# Now, Naive solution could be to loop through the numbers from 1 to Nth ugly number (to be found, N is input).
# But for that, we need to check if ith number is ugly number or not.
# Brute force way of doing that would be to check if that number divides 2, if not then check whether if that divides 3,
# and similarly for 5, and keep dividing and finally if it gives 1 as a result in any of the above three divisions, then yes it's an ugly number
# otherwise not, so in this case overall time complexity would be more than 0(N* LOG(N)).
# ---------------------------------------------------------------------------------------------
# Can we do better ? , especially in case of range queries like ugly(4) ? ugly (5) ? ugly (100).....
# So, we need to precompute the ugly numbers and use it to answer queries in case of range queries in 0(1).
# If we observe that earlier what we did, we keep checking if any of 2, 3, 5 divides it and then consider it and move for next number.
# So, we can actually use some already known information : that is the table of 2, 3, 5 and their multiples computed each time based on the condition
# that whichever is found to be minimum among them and use it to fill that place in the extra temp array.
# so, we apply 1-d DP array logic, where every subproblem is asking the question for that position's ugly number that means for computing nth ugly
# number, we need to know if n-1 is a ugly number is not, and for that we need to know if n-3 is ugly number or not ?
# base case is assuming "1" is a ugly number.
# ---------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(1)

# Now let's say if the primes are not fixed as earlier one and it is dynamic input array containing any number of primes.
# So, now we need to create a dynamic array for iterators (i2, i3, i5....) and also for next_i2, next_i3, next_i5.....
# everytime, we get min of iterators array and update both iterators and next_i2.....values...
# REST LOGIC WILL BE SAME.
# ----------------------------------------------------------------------------------------------

def compute_ugly_num(n):

    dp = [0] * n
    dp[0] = 1

    i2, i3, i5 = 0, 0, 0  # these are pointing to the tables of 2, 3, 5.....
    next_i2, next_i3, next_i5 = 2, 3, 5 # next is giving us the actual value from multiplication table...

    next_ugly = None
    for i in range(1, n):

        next_ugly = min(next_i2, next_i3, next_i5)
        dp[i] = next_ugly

        if next_ugly == next_i2:
            i2 += 1
            next_i2 = dp[i2] * 2
        if next_ugly == next_i3:
            i3 += 1
            next_i3 = dp[i3] * 3
        if next_ugly == next_i5:
            i5 += 1
            next_i5 = dp[i5] * 5

    return dp[n-1]


print(compute_ugly_num(150))
