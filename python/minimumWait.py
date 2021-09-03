# Input: [3,2,1,2,6]

def minimumWaitingTime(queries):
	# Maybe just sort these... longest goes last....
	# That worked... O(n) it is
	new = sorted(queries)
	total = 0
	placeholder = 0
	for i in range(1, len(new)):
		placeholder += new[i-1]
		total += placeholder
		
	return total