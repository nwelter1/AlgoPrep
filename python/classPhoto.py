def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	topRow = None
	bottomRow = None
	if redShirtHeights[0] > blueShirtHeights[0]:
		topRow = redShirtHeights
		bottomRow = blueShirtHeights
	elif redShirtHeights[0] < blueShirtHeights[0]:
		topRow = blueShirtHeights
		bottomRow = redShirtHeights
	else:
		return False
	
	for i in range(1,len(topRow)):
		if topRow[i] < bottomRow[i]:
			return False
	return True