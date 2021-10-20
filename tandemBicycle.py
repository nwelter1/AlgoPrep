def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    counter = 0
    if not fastest:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        for i in range(len(redShirtSpeeds)):
            if redShirtSpeeds[i] > blueShirtSpeeds[i]:
                counter += redShirtSpeeds[i]
            else:
                counter += blueShirtSpeeds[i]
        return counter
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse=True)
        for i in range(len(redShirtSpeeds)):
            if redShirtSpeeds[i] > blueShirtSpeeds[i]:
                counter += redShirtSpeeds[i]
            else:
                counter += blueShirtSpeeds[i]
        return counter