import random


def create_list(N, K):
  numbers_list = []
  for i in range(N):
    numbers_list.append(random.randint(0, K - 1))
  numbers_list.sort()
  return numbers_list


def binary_rec(L, left, right, y):
  if right >= left:
    mid = left + (right - left) // 2
    if L[mid] == y:
      return mid
    if L[mid] > y:
      return binary_rec(L, left, mid - 1, y)
    return binary_rec(L, mid + 1, right, y)
  return None


initlist = create_list(10, 100)
print(initlist)
targetnumber = initlist[random.randint(0, len(initlist) - 1)]
print("Randomised number:", targetnumber)
print('Occurs at index:', binary_rec(initlist, 0, len(initlist), targetnumber))