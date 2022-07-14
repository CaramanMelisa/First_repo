'''
13. Functie care primeste o lista de cifre (adica doar 0-9)
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
lista2=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def dicti(lista):
    for nr in lista:
        if nr in lista:
            nr+=1
            dictionar=dict(zip(lista, lista2))
    return dictionar
print(dicti([4,3,2,2,3,9,7]))

