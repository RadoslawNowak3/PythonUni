l1 = [10, 20, 30, 40, 50, 90]
l2 = [10, 20, 30, 50, 40, 70]
my_list = []
for i in range(0,len(l1)):
    for j in range (0,len(l2)):
        if(l1[i]==l2[j]):
            if l1[i]in my_list:
                break
            my_list.append(l1[i])
            break
print("Czesc wspolna sekwencji")
print(my_list)
my_list2 = l1
for i in range(0,len(l2)):
    if not l2[i] in my_list2:
        my_list2.append(l2[i])
my_list2 = sorted(my_list2)
print("Wszystkie elementy z sekwencji")
print (my_list2)