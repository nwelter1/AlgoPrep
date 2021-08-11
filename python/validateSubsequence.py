# Solution 1:
def isValidSubsequence(array, sequence):
    idxOG = 0
    idxSeq = 0
    while idxOG < len(array) and idxSeq < len(sequence):
        if array[idxOG] == sequence[idxSeq]:
            idxSeq +=1
        idxOG += 1
    return idxSeq == len(sequence)