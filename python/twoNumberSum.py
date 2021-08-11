# Solution 1: nested For Loops
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i],array[j]]
	return []

# Solution 2: 2 pointers
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		j = len(array)-1
		while i<j:
			if array[i] + array[j] == targetSum:
				return [array[i],array[j]]
			j -= 1
	return []