# tell(), seek() will allow us to handle file pointers.
# seek(offset, whence) method by default defines offset and whence as 1.
# whence : 0 => from beginning of file
# whence : 1 => from crrent pos
# whencee  : 2 => from end of file
# so offset can be +, -
# but this whence is only defined for "0" for normal files
# but other values of whence for seeks is defined for byte modes operation.

with open("C:/Users/DELL/Desktop/output.txt", 'ab') as file:
    print(file.tell())
    file.seek(-5, 2)
    file.write(b'0123456789abcdef')
