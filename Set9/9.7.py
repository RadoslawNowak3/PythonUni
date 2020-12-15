from BinarySearchTree import *

BST_1 = Node(45)
BST_1.insert(Node(15))
BST_1.insert(Node(144))
BST_1.insert(Node(123))
BST_1.insert(Node(24))
BST_1.insert(Node(42))
BST_1.insert(Node(64))
BST_1.insert(Node(0))
BST_1.insert(Node(4))
print("Min value in tree:", bst_min(BST_1))
print("Max value in tree:", bst_max(BST_1))
BST_2 = Node(None)
print("Min value in tree:", bst_min(BST_2))
BST_3 = None
print("Min value in tree:", bst_min(BST_3))