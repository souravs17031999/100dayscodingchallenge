# Program to match the words in the dictionery matching the Camel Case pattern.
# Input:
# 2
# 8
# Hi Hello HelloWorld HiTech HiGeek HiTechWorld HiTechCity HiTechLab
# HA
# 3
# WelcomeGeek WelcomeToGeeksForGeeks GeeksForGeeks
# WTG
# ---------------------------------------------------------------------------------------------------

#code

from sys import stdin, stdout

def camel_case_match(word, n, pattern):

    count = {}

    for i in range(n):

        res = []
        for j in range(len(word[i])):

            if ord(word[i][j]) >= 65 and ord(word[i][j]) <= 90:
                res.append(word[i][j])
                temp = "".join(res)
                if temp not in count:
                    count[temp] = [word[i]]
                else:
                    count[temp].append(word[i])

    res = []
    for key, value in count.items():
        if key == pattern:
           for i in value:
               res.append(i)

    print(count)
    return " ".join(res)


if __name__ == '__main__':

    print(camel_case_match(['Hi', 'Hello', 'HelloWorld', 'HiTech', 'HiGeek', 'HiTechWorld', 'HiTechCity', 'HiTechLab'], 8, 'HT'))
