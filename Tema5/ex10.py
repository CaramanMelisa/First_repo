'''
10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
'''
def nr_si_set(x, y):
    if x not in y:
        y.add(x)
        print('am adaugat numarul nou in set')
        return True
    else:
        print('nu am adaugat numarul in set. Acesta exista deja')
        return False
print(nr_si_set(6, {7 ,99, 90}))