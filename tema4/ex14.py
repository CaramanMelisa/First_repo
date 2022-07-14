'''
14.
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''
numar=1
x= int(input('Introduceti un numar: '))
for numar in range(1, x+1):
    for numar2 in range(1, numar+1):
        print(numar, end="")
    print()


