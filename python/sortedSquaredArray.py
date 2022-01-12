# Easy solution - list comp + sorted()
def sortedSquaredArray(array):
    return sorted([x**2 for x in array])

# Sorting without build in method (Bubble Sort)
def sortedSquaredArray(array):
    array2 = [x**2 for x in array]
	#Bubble sorting instead of built-in
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array2)-1):
            if array2[i] > array2[i+1]:
                array2[i], array2[i+ 1] = array2[i+ 1], array2[i]
                isSorted = False
    return array2

# Optimal solution: O(n) | O(n)
# O(n) time | O(n) space
def sortedSquaredArray(array):
    if len(array) == 1:
        return [array[0]**2]
    output_arr = [_ for _ in range(len(array))]
    i = 0
    j = len(array) - 1
    new_idx = len(output_arr) - 1
    while i <= j:
        if i == j and new_idx == 0:
            output_arr[new_idx] = array[j]**2
            j -= 1
        elif abs(array[i]) > abs(array[j]):
            output_arr[new_idx] = array[i]**2
            i += 1
            new_idx -= 1
        elif abs(array[j]) > abs(array[i]):
            output_arr[new_idx] = array[j]**2
            j -= 1
            new_idx -= 1
        else:
            output_arr[new_idx] = array[j]**2
            new_idx -= 1
            output_arr[new_idx] = array[i]**2
            new_idx -= 1
            j-=1
            i+=1
    return output_arr