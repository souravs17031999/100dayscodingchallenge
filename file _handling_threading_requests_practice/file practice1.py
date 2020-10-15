# Program for showing file handling.

# reading files
with open("dsa_today.txt", 'r') as file:
    data = file.read().split("\n")
    for line in data:
        print(line)

# NOTE : read(n), n is bytes/chars read from file, by default
# all the file will be written.
# readline() reads one by one line.
# readlines() reads all lines and returns as list.


# writing files
with open("C:/Users/DELL/Desktop/output.txt", 'w') as file:
    file.write("Hello World !")
    file.write("\n")
    file.write("Hello World !")

# write() writes one line.
# writelines() writes all the strings of list in one time.

# appending instead of writing
with open("C:/Users/DELL/Desktop/output.txt", 'a') as file:
    file.write("Hello World !")
    file.write("\n")
    file.write("Hello World !")

# NOTE: default "r", "w" means "rt", "wt" means in text mode.
# we can also do it in byte mode
# "rb", "wb"

# More than one mode in the same program : "r+" : read+write
# "a+" : read + append
# "r+" : read + write

# Byte modes : "rb", "wb"

with open("dsa_today.txt", 'rb') as file:
    data = file.readlines()
    for line in data:
        print(line)

# Combining multiple reads and writes

d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
