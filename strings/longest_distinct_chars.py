# Program to compute longest substring having all distinct characters (no repeating characters)
# EX.
# T =  2
# abababcdefababcdab => 6 => "abcdef"
# geeksforgeeks => 7 => "eksforg"
# ------------------------------------------------------------------------------------------------
# Here, Niave solution will be to generate all the substrings and check if any char repeat, then don;t take into account
# but if chars don't repeat, then take this and update the max length obtained so far.
# But this will take 0(N^3) and Space complexity : O(min(n, m)).
#
# Now, let's use window sliding technique in combination with hashtable (sets)
# TIME : 0(N), and Space complexity : O(min(n, m))
#
# Here, we can observe that atmost every element is visited at most 2 times one by right and one by left pointer, so overall it's 0(N) but avergae it would be 0(2*N), 
# So, can we do it in one pass such that left pointer is directly jumped to correct location instead of traversing left one by one..
# We can use HashMap in the form :  {char:left_ptr}, which means current char, left_ptr is basically the last occurence of seeing that char in the string.
# So, we can keep updating the char as soon as we see it in the substring.
# This time, when we see the same char in the hashmap, we can simply jump left pointer to value of hashmap + 1, only when it is in the current range of sliding window.
# It would be in 0(N) time, space : 0(N).
# -------------------------------------------------------------------------------------------------

#code
from sys import stdin, stdout

def main(s):

    start, end = 0, 0
    count = set()
    max_len = 0
    while end < len(s):

        if s[end] not in count:
            count.add(s[end])
            max_len = max(max_len, len(count))
            end += 1
        else:
            count.remove(s[start])
            start += 1

    return max_len

if __name__ == '__main__':
    t = int(stdin.readline().strip())
    for i in range(t):
        stdout.write(str(main(stdin.readline().strip())))
        stdout.write('\n')
