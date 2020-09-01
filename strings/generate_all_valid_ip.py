# Program for generating all the valid IP's from the given input string.
# Here, important thing is to we can use recursion + backtracking or iterative, both will take almost same complexity but main
# point is that overall complexity will be constant 0(1) as total ip addresses generated will be constant 0(2^32) ip addresses.
# ----------------------------------------------------------------------------------------------------------------------------------

def is_valid(s):

    s = s.split(".")
    for i in s:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True

def convert(s):

    n = len(s)
    if n > 12:
        return []

    s_new = s
    res = []
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                s_new = s_new[:k] + '.' + s_new[k:]
                s_new = s_new[:j] + '.' + s_new[j:]
                s_new = s_new[:i] + '.' + s_new[i:]

                if is_valid(s_new):
                    res.append(s_new)

                s_new = s
    return res

A = "25525511135"
# B = "25505011535"
print(convert(A))
# print(convert(B))
