# Program for improving string matching algorithm.
# Idea is similar to window sliding method used in naive matching, but now we are computing hashes,
# first precomputing for pattern and used it to match it for hashes computed for all sliding windows
# in the string text and when it matches, then we go for full comparison of all characters one by one.
# Best and Average :TIME => 0(M), M, N Is lenght of string.
# Worst case complexity : TIME : 0(M*N)
# -----------------------------------------------------------------------------------------------------
# NOTE : Much more asymtodic runtimes are dependent upon how we take and compute hash of the string.
# For good efficient hashing :
# hash : sigma : s[i].p^i % m
# where p and m are important parameters.
# p :- 31 if only lower case letters, if all letters, p = 53.
# m : 10^9 + 9 (very large prime number)
# -------------------------------------------------------------------------------------------------------
# Pseudo code
function RabinKarp(string s[1..n], string pattern[1..m])
    hpattern := hash(pattern[1..m]);
    for i from 1 to n-m+1
        hs := hash(s[i..i+m-1])
        if hs = hpattern
            if s[i..i+m-1] = pattern[1..m]
                return i
    return not found

# ---------------------------------------------------------------------------------------------------------s
# Using rolling hash function for RabinKarp algorithm string matching :
# using 256 as the base, and 101 as the prime modulus is:
// ASCII a = 97, b = 98, r = 114.
hash("abr") =  [ ( [ ( [  (97 × 256) % 101 + 98 ] % 101 ) × 256 ] %  101 ) + 114 ]   % 101   =  4

//           old hash   (-ve avoider)*   old 'a'   left base offset      base shift    new 'a'    prime modulus
hash("bra") =     [ ( 4   + 101         -  97 * [(256%101)*256] % 101 ) * 256         +    97 ] % 101              =  30
