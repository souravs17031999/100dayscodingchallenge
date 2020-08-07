def get_hash(s):
    p = 31
    m = 10 ** 9 + 9
    hash_value = 0
    power = 1
    for i in range(len(s)):
        hash_value += (ord(s[i]) * power) % m
        power = (power * p) % m

    return hash_value

if __name__ == '__main__':
    print(get_hash("souravkumar"))
