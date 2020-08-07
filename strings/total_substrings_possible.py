# So, given a string, compute total possible substrings in it.
# So, we can see for all substrings possible,
# length can be decreased one by one , then to 1,
# n + (n - 1) + (n - 2) + (n - 3) ...... + 2 + 1
# n * (n + 1) // 2 => total substrings possible.
# also, if empty substring is also valid, then
# (n * (n + 1) // 2) + 1
