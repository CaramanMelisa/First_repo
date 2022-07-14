'''
9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale
'''
def comparare(x, y):
    if x > y:
        print (f'Primul numar {x} este mai mare decat al doilea nr {y}')
    elif x<y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print('Numerele sunt egale')
print(comparare(565, 3422))