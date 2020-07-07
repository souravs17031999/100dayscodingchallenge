# Print the camelcase individual words for a given string.

def CamelPrint(s):
    count = 0
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            print()
            print(s[i], end = "")
        else:
            print(s[i], end = "")

if __name__ == '__main__':
    s = "IAmACompetitiveProgrammer"
    CamelPrint(s)
