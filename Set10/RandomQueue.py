import random


class RandomQueue:

  def __init__(self):
    self.items = []

  def __str__(self):
    return str(self.items)

  def put(self, item):
    if self.is_full():
      raise OverflowError("Queue is full!")
    self.items.append(item)

  def get(self):
    if self.is_empty():
      raise ValueError("Queue is empty!")
    index = random.randint(0, len(self.items) - 1)
    temp = self.items[-1]
    self.items[-1] = self.items[index]
    self.items[index]= temp
    return self.items.pop()

  def is_empty(self):
    return not self.items

  def is_full(self):
    return False

  def clear(self):
    self.items = []