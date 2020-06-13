# Short idea for modular exponentiation, logic is same for bitwise exponentiation.
# IDEA: approach is same as already done for fast exponentiation but here we will also include modulus for avoiding overflows
# TIME : 0(log(B))

def mod_exp(a, b, m):

    ans = 1
    a = a % m

    if a == 0:
        return 0

    while b > 0:
        if b & 1:
            ans = (ans * a) % m
        a = (a * a) % m
        b = b // 2
    return ans


print(mod_exp(2, 10, 1000000000))
