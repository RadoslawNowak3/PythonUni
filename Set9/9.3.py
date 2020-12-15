from DoubleList import *

DL_test = DoubleList()

for index in range(12):
  DL_test.insert_tail(Node(index))

print("My list:", DL_test)
node1 = DL_test.find_min()
node2 = DL_test.find_max()
node3 = Node(5)
node4 = Node(25)
DL_test.remove(node1)
print("Removal of first element:", DL_test)
DL_test.remove(node2)
print("Removal of last element:", DL_test)
DL_test.remove(node3)
print("Removal of node with the value of 5", DL_test)
DL_test.remove(node4)
print("Removal of non-existent node", DL_test)
print("Min in list:", DL_test.find_min())
print("Max in list:", DL_test.find_max())
DL_test.clear()
print("Cleared list:", DL_test)