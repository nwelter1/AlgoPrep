def insertionSort(array):
    for i in range(1,len(array)):
        j = i
        while j > 0:
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1
            else:
                break
    return array

print(insertionSort([90,4,50,6,7,88]))