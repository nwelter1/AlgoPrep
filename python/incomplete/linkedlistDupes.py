# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(LinkedList):
    seen = {}
    current = LinkedList
    prev_node = LinkedList
	
    while current.next is not None:
	    if current.value in seen:
		    prev_node.next = prev_node.next.next
	    else:
		    seen[current.value] = 'seen'
	    prev_node = current
	    current = current.next
    if current.next is None and current.value in seen:
	    prev_node.next = None
    return LinkedList