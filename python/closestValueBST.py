# O(n) O(n)

def findClosestValueInBst(tree, target):
	closest = float('inf')
	q = [tree]
	while len(q):
		node = q.pop(0)
		if abs(target - node.value) < abs(target - closest):
			closest = node.value
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
	return closest
		


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

