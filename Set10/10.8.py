from RandomQueue import *

randomQueue = RandomQueue()

for i in range(20):
  randomQueue.put(i)
print('Queue:', randomQueue)

while not randomQueue.is_empty():
  print("Removing element:", randomQueue.get())
  print('Queue:', randomQueue)