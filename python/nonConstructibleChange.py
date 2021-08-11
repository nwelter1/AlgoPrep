def nonConstructibleChange(coins):
	coins.sort()
	current_seen = 0
	for coin in coins:
		if coin > current_seen +1:
			return current_seen + 1
		else:
			current_seen += coin
	return current_seen + 1