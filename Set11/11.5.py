# Gnome Sort to algorytm sortowania o zlozonosci O(N^2) ktory polega na zamianie sasiednich elementow (jesli nie sa w
# odpowiedniej kolejnosci) w celu posortowania calej listy.
import random
def gnomeSort(arr, n):
   index = 0
   while index < n:
      if index == 0:
         index = index + 1
      if arr[index] >= arr[index - 1]:
         index = index + 1
      else:
         arr[index], arr[index-1] = arr[index-1], arr[index]
         index = index - 1
   return arr


array = []
n=20
for i in range(n):
    array.append(i)
random.shuffle(array)
print("Unsorted sequence is:")
print(array)
arrayy = gnomeSort(array, n)
print ("Sorted sequence is:")
print(arrayy)