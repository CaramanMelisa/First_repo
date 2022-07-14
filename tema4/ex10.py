'''
10.
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
new_numere=[]
for numar in numere:
    if numar > 0:
        numar=-(numar)
    new_numere.append(numar)
print(new_numere)