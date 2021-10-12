def selectionSort(array):
    for i in range(len(array)-1):
	    low = i
	    for j in range(i+1, len(array)):
		    if array[low] > array[j]:
			    low = j
			
	    array[low], array[i] = array[i], array[low]
    return array