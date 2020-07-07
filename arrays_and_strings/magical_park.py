# Program, Piyush is lost in a magical park which contains N rows and M columns.In order to get out of park safely and return home, he needs
# atleast K amount of strength.Given a N by M pattern, your task is to find weather Piyush can ever escape the park.
#Piyush enters the park with strength S. The park is filled with some obstacles denoted by ‘.’ , some magical beans denoted by ‘*’ and some #
# blockades denoted as ‘#’. If he encounters an obstacle (.) , strength decreases by 2. If he encounters a magic bean (' * ') , his strength
#increases by 5. Piyush can only walk row wise, so he starts from left of a row and moves towards right and he does this for every row.
# However when he encounters a blockade (#) , he cannot go any further in his current row and simply jumps to the start of a new line without
# losing any strength. Piyush requires a strength of 1 for every step. His strength should always be greater than K while traversing or else
#Piyush will get lost
# DETERMINE IF PIYUSH WILL GET OUT OF THE PARK OR NOT ?

def MagicPark(mat, m, n, k, s):
    for i in range(m):
        for j in range(n):

            if s < k:
                return 0

            if mat[i][j] == '*':
                s += 5
            elif mat[i][j] == '.':
                s -= 2
            else:
                break

            if j != n - 1:
                s -= 1

    return 1, s

if __name__ == '__main__':
    s = [['.', '.', '*', '.'], ['.', '#', '.', '.'], ['*', '*', '.', '.'], ['.', '#', '*', '*']]
    print(MagicPark(s, 4, 4, 5, 20))
