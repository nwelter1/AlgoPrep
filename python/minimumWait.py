def minimumWaitingTime(queries):
	# Maybe just sort these... longest goes last.... everything else will still count regardless...
	# That worked! O(n)
	new = sorted(queries)
	total = 0
	placeholder = 0
	for i in range(1, len(new)):
		placeholder += new[i-1]
		total += placeholder
		
	return total