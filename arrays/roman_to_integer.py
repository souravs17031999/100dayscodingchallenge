# program to convert roman literals to integer
# d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} dictionery of roman to numeric
# logic is to traverse the string one by one, and if value of first char is less than second one, then calulate the difference between the two values and sum up them,
# otherwise sum the current position values.
# also, return the exact sum only if the above pattern is not followed, otherwise sum the last char value also with the overall sum calculated.
# to control the above behaviour, we are using flag var

def convert_rom_to_int(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    i = 1
    # flag to control if returning value will be sum or sum + last char
    flag = 1
    # traversing from start of string till one less than last char
    while i <= len(s) - 1:
        # if first one is less than second one, then we need to sum up the difference between these values like 'CM' : val(M) - val(C) = 1000-100 = 900
        if d[s[i - 1]] < d[s[i]]:
            if i == len(s) - 1:
                flag = 0
            sum = sum + (d[s[i]] - d[s[i - 1]])
            # skipping next two char due to already checked char
            i += 2
        # otherwise, sum up the current char value
        else:
            sum = sum + d[s[i - 1]]
            # skipping only one char
            i += 1
    # return the sum only if pattern is followed, otherwise return the sum with adding up the last char also
    return sum + flag*d[s[-1]]

if __name__ == '__main__':
    assert convert_rom_to_int('MCMXCIV') == 1994
    assert convert_rom_to_int('LVIII') == 58
    assert convert_rom_to_int('IX') == 9
    assert convert_rom_to_int('I') == 1
    assert convert_rom_to_int('III') == 3
    assert convert_rom_to_int('MCMIV') == 1904
