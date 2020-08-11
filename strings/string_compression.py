# program to compress the string in a particular fashion, instead of printing all the repeated chars in a string,
# we need to take only the count of the repeated char and a count of just that char.

def compress_string(s):
    result, count = "", 1
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            result = f"{result}{str(count)}{prev}"
            #result += prev
            prev = s[i]
            count = 1

    result = f"{result}{str(count)}{prev}"
    print(result)

if __name__ == '__main__':
    s = "aaabbccds"
    compress_string(s)
