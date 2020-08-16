# There can really huge number of cases where string hashing is really powerful.

# polynomial rolling hash function
# hash(s) = sigma(s[i] * p^i) % m
def get_hash(s):
    p = 31  # if we are using both ascii lower and upper case letters, then use  p = 53.
    m = 10 ** 9 + 9
    hash_value = 0
    power = 1
    for i in range(len(s)):
        hash_value += (ord(s[i]) * power) % m
        power = (power * p) % m

    return hash_value

# this is a simple hash function
def get_hash(key):
    sum = 0
    for i in key:
        sum += ord(i)
    return sum % 10

if __name__ == '__main__':
    print(get_hash("souravkumar"))
