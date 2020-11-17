L = [3, 5, 4]; L = L.sort()
# Bledem jest przyrownanie listy, robiac to otrzymujemy liste pusta bo metoda ta nie zwraca zadnej wartosci, by otrzymac
# pozadany wynik nalezy wywolac ja bez przyrownania.
# Poprawne rozwiazanie:
L = [3, 5, 4]
L.sort()
print(L)
# x, y = 1, 2, 3
# Bledem tutaj jest przypisywanie trzech wartosci do dwoch elementow, nalezy tutaj dodac trzeci element badz usunac wartosc
# Przykladowe poprawne rozwiazanie:
x,y,z = 1,2,3
##############
 X = 1, 2, 3; X[1] = 4
# Bledem jest wykonywanie prob zmian wartosci obiektu typu tuple, nalezy wczesniej przekonwertowac go na jakis inny typ
# Przykladowe rozwiazanie:
X = 1, 2, 3;
X = list(X)
X[1]=4
print(X)
##############
X = [1, 2, 3]; X[3] = 4
# Bledem jest odwolanie do indeksu wykraczajacego poza rozmiar obiektu - indeksowanie zaczyna sie od 0, wiec ostatnim
# indeksem w tym przypadku jest 2
# Przykladowe rozwiazanie:
X = [1, 2, 3]; X[2] = 4
##############
X = "abc" ; X.append("d")
# Bledem jest wywolanie metody append dla obiektu typu string ktory nie jest lista
# Przykladowe rozwiazanie:
X = "abc"
X += "d"
##############
# Pow jest funkcja ktora wymaga dwoch argumentow a mapa wymaga mozliwosci iterowania po argumentach, dlatego nalezy
# przy wywolaniu funkcji wykorzystac dwa przedzialy lub uzyc innej funkcji
# Przykladowe rozwiazanie:
L = list(map(pow, range(8), range(8)))
print(L)