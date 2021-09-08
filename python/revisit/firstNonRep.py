def firstNonRepeatingCharacter(string):
    # SUper Naive Solution
    idx_dict = {}
    answer = -1
    for i in range(len(string)):
	    if string[i] in idx_dict:
		    idx_dict[string[i]] = -1
	    else:
		    idx_dict[string[i]] = i
	
    for i in range(len(string)):
	    if idx_dict[string[i]] > -1 and answer == -1:
		    answer = i
	    elif idx_dict[string[i]] > -1 and idx_dict[string[i]] < answer:
		    answer = i
    return answer