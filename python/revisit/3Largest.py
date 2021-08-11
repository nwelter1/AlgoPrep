# 3 larget nums in array without sorting OG input
def findThreeLargestNumbers(array):
    top3 = []
    for i in range(len(array)):
        if len(top3) < 3:
            top3.append(array[i])
            top3.sort()
        else:
            if array[i] > top3[0]:
                top3[0] = array[i]
                top3.sort()
    return top3

# Solution 2
def findThreeLargestNumbers(array):
    return sorted([x for x in array])[-3:]