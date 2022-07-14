'''
8.
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum=0
for numar in numere:
    numar+=1
    sum= sum + numar
print(f'Suma numerelor este {sum}')

