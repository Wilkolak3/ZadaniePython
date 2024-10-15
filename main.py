from Tablica import Tablica

tab = Tablica(3)
tab.wypelnij(1, 10)
print("Tablica: ", tab)

mini = tab.minimum()
print("Minimum: ", min)

maks = tab.maksimum()
print("Maksimum: ", maks)


maks2 = tab.maksimum2()
print("Maksimum2: ", maks2)

szukana = 5
index = tab.znajdz(szukana)
print("Wartość szukana: ", szukana, "\n Index: ", index)


