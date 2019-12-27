# Program for finding sum of n digit numbers divisible by p

# logic is to firstly find out the first and last number of that required range, like for 1 digit - it's 1 to 10, then for two digit, it's 10 to 100 , similary 100-to 1000 for three digit numbers.
# Then the second thing is that can find out the first number and last number divisible by given number , and it follows from the observation of this series is A.P and then hence , we can calculate no of terms using formula for nth term, a(n) = a + (n - 1) * d and then use second formula for calculating sum of the series : s = (n/2)*[a + l] / 2
def sum_div(n, p):
    # calculate first and second for the range
    first_num = pow(10, n - 1)
    last_num = pow(10, n)
    # calculate those first and last which are divisible
    first_dig = first_num - first_num % p + p
    last_dig = last_num - last_num % p
    # count of those all numbers in this sequence
    count_numbers = ((last_dig - first_dig) / p) + 1
    # return the sum now 
    return ((count_numbers) * (first_dig + last_dig) / 2)

print(sum_div(3, 7))
