# Solution 1: O(n) | O(1)
def isValidSubsequence(array, sequence):
    idxOG = 0
    idxSeq = 0
    while idxOG < len(array) and idxSeq < len(sequence):
        if array[idxOG] == sequence[idxSeq]:
            idxSeq +=1
        idxOG += 1
    return idxSeq == len(sequence)

# Solution 2 O(n) | O(1)
def isValidSubsequence(array, sequence):
    i = 0
    j = 0
    while i < len(array):
    	if array[i] == sequence[j]:
    		i += 1
            j += 1
            if j == len(sequence):
					return True
		else:
			i += 1
	return False