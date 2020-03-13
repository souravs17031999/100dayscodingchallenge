# implementing randomized version of QuickSort 
import random
def partition(arr,low,high):
	i = low - 1
	pivot = arr[high]
	for j in range(low , high):
		if arr[j] < pivot:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

def partitionr(arr, low, high):
	randpivot = random.randrange(low, high)
	arr[low], arr[randpivot] = arr[randpivot], arr[low]
	return partition(arr, low, high)

def quicksort(arr, low, high):
	if low < high:
		pi = partitionr(arr, low, high)
		print(pi)
		print("going for left sub array")
		quicksort(arr, low, pi - 1)
		print("going for right sub array")
		quicksort(arr, pi + 1, high)

if __name__ == '__main__':
	arr = [10, 7, 8, 9, 1, 5]
	quicksort(arr, 0, 5)
	print(arr)
