# Problem description : Prateek Bhaiya decided to give 100% scholarships to the needy students by taking an admission test. However in order
# to avoid any losses at the institute, he came up with a solution. Coding Blocks has N students and M discount coupons. A student will get
# 100% waiver if he gets X discount coupons. However in order to get more discount coupons in addition to those M , Bhaiya decided that some
# students who perform badly in the admission tests, need to pay additional amount equivalent to Y discount coupons, i.e. good students earn
# discount coupons and weak students need to pay coupons to get admission.
# Find out the maximum number of students who can get 100% waiver in their admission fees.
# Note : Bhaiya will try his best to give 100% discount to maximum students possible.
# So, if we observe here, we are able to estimate some possible answer that it will lie within 0 - N.
# That also tells again, we have a search space 0, 1, 2, .... N which is monotonic in nature such that if we are able to give out
# scholarships to atleast X number of students, then we are also able to give scholarships to lesser than X students and in this way
# we can keep reducing our search space and converge to maximum possible value.
# TIME : 0(lg(N)), SPACE : 0(1).

from sys import stdin, stdout


# function to check whether it;s possible to give out scholarships to total "mid" number of students
def isPossible(n, m, x, y, mid):
    # so, total scholarships needed will be mid*x and we know available scholarships will be m (as given) and also
    # remaining (n - mid) as less than x we can already do, and since y amount we can get from student,
    # so we also have total scholarships (n - mid) * y which makes total m + (n - mid) * y.

    return mid * x <= m + (n - mid) * y

# function to compute maximum scholarships
def compute_scholarship(n, m, x, y):
    # defining search space
    start, end = 0, n
    ans = 0
    # applying bin search
    while start <= end:

        mid = (start + end) // 2
        if isPossible(n, m, x, y, mid):
            # if it's possible to give out scholarships to all students, then we will try to go for more greater values
            ans = mid
            start = mid + 1
        else:
            # if not possible, then we try for lesser values 
            end = mid - 1

    return ans

if __name__ == '__main__':
    n, m, x, y = 5, 10, 2, 1
    print(compute_scholarship(n, m, x, y))
