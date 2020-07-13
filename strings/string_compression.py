# program to compress the string in a particular fashion, instead of printing all the repeated chars in a string,
# we need to take only the count of the repeated char and a count of just that char.

def compress_string(s):
    temp, count = s[0], 1
    print(temp, end = "")
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            temp = s[i]
            print(f"{count}{temp}", end = "")
            count = 1
    print(count)

if __name__ == '__main__':
    s = "aaabbccds"
    compress_string(s)
