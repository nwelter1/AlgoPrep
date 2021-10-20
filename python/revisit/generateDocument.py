def generateDocument(characters, document):
    char_dict = {}
    doc_dict = {}
    
    for item in characters:
        if item in char_dict:
            char_dict[item] += 1
        else:
            char_dict[item] = 1
    for item in document:
        if item in doc_dict:
            doc_dict[item] += 1
        else:
            doc_dict[item] = 1
    
    for letter in document:
        if letter in char_dict:
            if char_dict[letter] < doc_dict[letter]:
                return False
        else:
            return False
    return True