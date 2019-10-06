# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Google.
# 
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# 
# For example, given the following Node class
# 
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# The following test should pass:
# 
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

# Comma separates nodes
def serialize(root):
	# Will handle this pre-order (?)
	
	tree_string = root.data
	if root.left != None:
		tree_string += ',' + serialize(root.left)
	else:
		tree_string += ',' + 'NULL'
	if root.right != None:
		tree_string += ',' + serialize(root.right)
	else:
		tree_string += ',' + 'NULL'
	
	return tree_string
	
def deserialize(s):
	
	cut_str = s.split(',')[0]
	remain_str = ','.join(s.split(',')[1:])
	
	root = Node(cut_str)
	if cut_str == 'NULL':
		return None, remain_str
	else:
		root.left, remain_str = deserialize(remain_str)
		root.right, remain_str = deserialize(remain_str)
	
	return root, remain_str
	
# For testing
def print_tree(root, indent = 0):
	for i in range(indent): print(" ", end = '')
	print(root.data)
	if root.left != None:
		print_tree(root.left, indent+1)
	if root.right != None:
		print_tree(root.right, indent+1)
		
def create_test_tree():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.right.left = Node(4)
	root.right.right = Node(5)
	return root
	

root = create_test_tree()
print_tree(root)

node = Node('root', Node('left', Node('left.left')), Node('right'))
print_tree(node)

s = serialize(node)
print(s)
node, s = deserialize(s)
print_tree(node)


# A slight punt, this might be easier in C rather than python
n, s = deserialize(serialize(node))
assert n.left.left.data == 'left.left'

