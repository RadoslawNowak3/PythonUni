import random

def create_list(N, K):
    numbers_list = []
    for i in range(N):
        numbers_list.append(random.randint(0, K - 1))
    return numbers_list


def linear_search(elements, search):
    occ = []
    for i in range(len(elements)):
        if elements[i] == search:
            occ.append(i)
    return occ


initlist = create_list(100, 10)
print(initlist)
targetnumber = initlist[random.randint(0, len(initlist) - 1)]
occurences = linear_search(initlist, targetnumber)
print("Randomised number:", targetnumber)
print("Occurs at indexes:", occurences)