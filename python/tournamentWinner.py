# Solution #1:

def tournamentWinner(competitions, results):
    a_dict = {}
    for i in range(len(competitions)):
        if results[i] == 0:
            index = 1
        else:
            index = 0
        if competitions[i][index] not in a_dict:
            a_dict[competitions[i][index]] = 1
        else:
            a_dict[competitions[i][index]] += 1
        
            
    return max(a_dict, key = a_dict.get) 