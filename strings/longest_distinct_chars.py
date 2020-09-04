# Program to compute longest substring having all distinct characters (no repeating characters)
# EX.
# T =  2
# abababcdefababcdab => 6 => "abcdef"
# geeksforgeeks => 7 => "eksforg"
# ------------------------------------------------------------------------------------------------
# Here, Niave solution will be to generate all the substrings and check if any char repeat, then don;t take into account
# but if chars don't repeat, then take this and update the max length obtained so far.
# But this will take 0(N^3).
# Now, let's use window sliding technique in combination with hashtable (sets)
# TIME : 0(N), SPACE : 0 (1)

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
