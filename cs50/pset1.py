def mario_block_right(n):
	for i in range(0, n):
		for j in range(0, n-i-1): # printing spaces
			print(" ", end = "")
		for k in range(0, i + 1): # printing stars
			print("*", end = "")
		print()

def mario_block_left(n):
	for i in range(0, n):
		for k in range(0, i + 1): # printing stars
			print("*", end = "")
		print()


def mario_tree(n):
	for i in range(0, n):
		for j in range(0, n-i-1): # printing spaces
			print(" ", end = "")
		for k in range(0, i + 1): # printing stars
			print("*", end = "")
		print(" ", end = "")
		for k in range(0, i + 1): # printing stars
			print("*", end = "")
		print()

if __name__ == '__main__':
	while(1):
		height = int(input("Mario Tree Height: "))
		if height <= 0:
			print("wrong value of height !")
		else:
			mario_tree(height)
			break	
