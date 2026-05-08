def quick_sort(array):

	if len(array) <= 1:
		return array
		
	pivot = array[0]
	lesser_array = [num for num in array[1:] if num <= pivot]
	greater_array = [num for num in array[1:] if num > pivot]

	return quick_sort(lesser_array) + [pivot] + quick_sort(greater_array)