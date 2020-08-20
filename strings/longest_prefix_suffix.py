# Program for computing longest prefix suffix lps array building for the given string.
# Often used as KMP preprocessing part for substring search.
# --------------------------------------------------------------------------------------
# In Below algorithm, i denotes longest suffix, and j denotes prefix matching with longest suffix.
# We assume pi[i] = 0, and start our algorithm with i = 1, and j = 0.
# And whenever s[i] and s[j] matches, we move both i, and j and set lps[i] = j + 1 as till j it has been matched : substring 0...j - 1
# but when they don't match, we set j at the last longest found prefix as till that has already matched, so we again start from there,
# so for going back to last matched substring, we use lps[j - 1] which tells the exactly same thing.
# TIME : 0(N), N IS LENGTh OF GIVEN STRING, SPACE : 0(N).
# ---------------------------------------------------------------------------------------

def build_lps(s):

    i, j = 1, 0
    n = len(s)
    lps = [0] * n
    while i < n:
        if s[i] == s[j]:
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    print(lps)
    return max(lps)

if __name__ == '__main__':
    print(build_lps("aaaa"))
