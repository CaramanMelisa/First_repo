'''
12.
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for numar in range(len(alte_numere)):
    for numar2 in range(numar + 1, len(alte_numere)):
        if alte_numere[numar] > alte_numere[numar2]:
            alte_numere[numar],\
            alte_numere[numar2] = alte_numere[numar2],\
            alte_numere[numar]
print(alte_numere)
