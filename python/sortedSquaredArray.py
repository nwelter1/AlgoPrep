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