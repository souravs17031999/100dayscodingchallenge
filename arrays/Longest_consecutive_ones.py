# Program to count maximum length of consecutive ones in a integer 

# naive solution will be to use two loops, one outer loop starting from every integer and inner loop to start from that integer to consecutive ones and count the ones.
# then take the overall max count which takes 0(N*N), where N is length of binary string converted for integer N.

# Efficient approach using sliding window
# in 0(N), where N is same as said above.

from sys import stdin, stdout
n = bin(int(stdin.readline().strip()))[2:]
stdout.write(n)
stdout.write("\n")
max_z = 0
temp = 0
for i in range(len(n)):
	if n[i] == '1':
		temp += 1
		max_z = max(max_z, temp)
	else:
		temp = 0
		
stdout.write(str(max_z))

# ----------------------------------------------------
# Another efficient approach using bitwise operation taking O(length of max ones consecutive)

stdout.write("\n")
x = int(stdin.readline().strip())
count = 0
while x :
	x = (x & (x << 1))
	count += 1

stdout.write(str(count))
