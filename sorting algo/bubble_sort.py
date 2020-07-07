from sys import stdin, stdout
def bubble_sort(arr, n):
	for i in range(n):
		flag = False
		for j in range(n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				flag = True

		if not flag:
			break
	for i in arr:
		stdout.write(f"{i}\n")

if __name__ == '__main__':
    arr = [-90, 12, -60, 900, 0]
    bubble_sort(arr, len(arr))
