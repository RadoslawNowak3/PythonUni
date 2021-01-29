Tematem projektu jest implementacja ADT Grafu oraz algorytmu Dijkstry do wyznaczania najkrótszej ścieżki.

Wybrany rodzaj implementacji grafu nieskierowanego - macierz sąsiedztwa
Wykorzystywane metody:
is_full(self) - bool, sprawdza, czy macierz została zapełniona
is_empty(self) - bool, sprawdza, czy graf jest pusty
add_vertex(self) - dodaje wierzchołek do grafu
has_vertex(self,index) - bool, sprawdza, czy wierzchołek o danym indeksie jest częścią grafu
copy_graph(self) - tworzy kopię grafu
complement_graph(self) - tworzy dopełnienie grafu
is_in_range(self,v1,v2)  - bool, sprawdza, czy indeksy nie wykraczają poza graf
has_edge(self, v1, v2) - bool, sprawdza, czy między wierzchołkami v1 i v2 istnieje krawędź
weight_edge(self, v1, v2) - zwraca wagę krawędzi między wierzchołkami v1 i v2 lub informuje o tym, że krawędź nie istnieje i zwraca -1
add_edge(self, v1, v2, value) - dodaje wierzchołek o wadze value między krawędziami v1 i v2 i inkrementuje zmienną przechowującą ilość krawędzi, jeśli podana waga wierzchołka jest ujemna zwraca -1 oraz informacje o niepoprawnej wadze, jeśli wierzchołek już istnieje albo podane indeksy wierzchołków wykraczają poza rozmiar grafu zwraca -2 i informację o błędzie
remove_edge (self, v1, v2) - usuwa krawędź między wierzchołkami v1 i v2 i dekrementuje zmienną przechowującą ilość krawędzi, jeśli graf nie ma krawędzi zwraca -1 i informację o tym fakcie, jeśli krawędź nie istnieje bądź indeksy wykraczają poza graf zwraca -2 i informację o tym fakcie
remove_vertex(self, index) - usuwa wierzchołek o danym indeksie odpowiedno przesuwając afektowane dane i dekrementuje zmienną przechowującą liczbę wierzchołków, jeśli graf jest pusty zwraca -1 i informację, jeśli wierzchołek o podanym indeksie nie istnieje zwraca -2 i informację.
print_graph(self) - wypisuje tablicę dwuwymiarową reprezentującą graf
print_edges(self) - wypisuje istniejące krawędzie w formie indeksów połączonych wierzchołków i wagi krawędzi między nimi
min_distance(self, visited, distance) - metoda pomocnicza wykorzystywana w algorytmie Dijkstry, znajduje i zwraca wierzchołek o najmniejszym kluczu(wartości krawędzi) który nie został jeszcze wykorzystany
dijkstra(self, source) - wyznacza długość najkrótszych ścieżek od źródła (wybranego wierzchołka) do wszystkich pozostałych wierzchołków grafu, po czym je wypisuje wraz z kosztem.
Wykorzystuje w tym celu dwie tablice - visited, przechowującą odwiedzone już wierzchołki oraz distance, przechowującą odległości do poszczególnych wierzchołków.
W momencie tworzenia tablica distance zapełniana jest nieskończonościami dla każdego wierzchołka z wyjątkiem źródła, dla którego wynosi 0, oraz tabela visited jest zapełniana False. Następnie algorytm określa do którego wierzchołka odległość jest najmniejsza i oznacza go jako odwiedzony, po czym aktualizuje tablicę odległości jeśli wartości krawędzi prowadzących do sąsiadów danego wierzchołka są mniejsze od aktualnie przechowywanych. Algorytm wykonuje się do momentu oznaczenia wszystkich wierzchołków jako odwiedzonych. Trzecia, dodatkowa tablica travel przechowuje indeksy wierzchołków z których podróżowano do danego wierzchołka.
Następnie algorytm wypisuje wierzchołki i odległość do nich od źródła oraz ścieżki które do nich prowadzą.