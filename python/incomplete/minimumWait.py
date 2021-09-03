def minimumWaitingTime(queries):
    # Write your code here.
	# put these numbers in an order that is long short long short etc
	
	# need a 2 pointer to go max min max min max min 
	# OR largest at the end and the others don't matter????
	# then loop through new arr
	
	#after in correct order...
	total = 0
	placeholder = 0
	for i in range(1,len(queries)):
		placeholder += queries[i-1]
		total += placeholder
		
	return total