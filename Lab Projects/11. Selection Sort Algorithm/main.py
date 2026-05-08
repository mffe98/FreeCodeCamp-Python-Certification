# Verbose Solution:
def selection_sort(array):
	if len(array) <= 1:
		return array
	for i, value in enumerate(array):
		min_value = value
		min_index = i
		for j, num in enumerate(array[i:], i):
			if num < min_value:
				min_value = num
				min_index = j
		if array[i] > array[min_index]:
			array[i], array[min_index] = array[min_index], array[i]
	return array

# Reduced to Simplest and Shortest:
def selection_sort(array):
    n = len(array)
    if n <= 1:
        return array
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j
        if array[min_index] < array[i]:
            array[i], array[min_index] = array[min_index], array[i]
    return array