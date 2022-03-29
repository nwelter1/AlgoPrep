# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(LinkedList):
	if not LinkedList:
		return None
	current = LinkedList
	
	while current.next:
		print(current.next)
		if current.value == current.next.value:
			current.next = current.next.next
		else:
			current = current.next
	return LinkedList