# Solution 1: nested For Loops (Quadratic)
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i],array[j]]
	return []

# Solution 2: 2 pointers O(n logn)
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		j = len(array)-1
		while i<j:
			if array[i] + array[j] == targetSum:
				return [array[i],array[j]]
			j -= 1
	return []

# Solution 3 - Linear O(2n)
def twoNumberSum(array, targetSum):
	a_dict = {}
	for i in range(len(array)):
		a_dict[array[i]] = targetSum - array[i]
	for num in array:
		if a_dict[num] in a_dict:
			if num == a_dict[num]:
				continue
			else:
				return [num, a_dict[num]]
	return []

# Best Solution - Linear O(n)
def twoNumberSum(array, targetSum):
	a_dict = {}
	for i in range(len(array)):
		if array[i] in a_dict:
			return [array[a_dict[array[i]]], array[i]]
		else:
			match = targetSum - array[i]
			a_dict[match] = i
	return []