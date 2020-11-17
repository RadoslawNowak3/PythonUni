x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
print (result)
# Kod w teorii jest poprawny, ale mozna pominac ostatni srednik w pierwszej linijce (lub oba zmieniajac nieco strukture)
# jak i nawiasy przy instrukcji warunkowej
# poprawiona wersja:
x=2; y=3
if x > y:
    result = x
else:
    result = y
############
for i in "qwerty": if ord(i) < 100: print (i)
# Bledem w tym kodzie jest nie zastosowanie wciec przez co program nie moze sie skompilowac
# poprawiony kod:
for i in "qwerty":
    if ord(i) < 100:
        print(i)
############
for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Ten kod dziala w porzadku, mozna przeniesc print do wciecia w kolejnej linijce dla lepszej przejrzystosci
for i in "axby":
    print (ord(i) if ord(i) < 100 else i)