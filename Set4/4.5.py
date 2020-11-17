def odwracanie_it(L, left, right):
    len = int((right-left)/2)
    for i in range(0,len):
        tmp = L[left+i]
        L[left+i] = L[right-i]
        L[right-i]=tmp
def odwracanie_rec(L, left, right):
    if left==right:
        return
    tmp = L[left]
    L[left] = L[right]
    L[right]=tmp
    odwracanie_rec(L, left + 1, right - 1)

example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odwracanie_it(example_list, 2, 10)
print(example_list)

example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odwracanie_rec(example_list, 2, 10)
print(example_list)