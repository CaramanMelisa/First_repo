'''
1.
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inverseaza ordinea folosind slicing si suprascrie aceasta lista
c. Printeaza varianta actuala (inversata)
d. Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
e. Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
'''
note_muzicale=['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale[::-1]
note_muzicale=note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
'''
2. 
De cate ori apare ‘do’?
'''
print(note_muzicale.count('do'))

'''
3.
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista
'''
l1=[3, 1, 0, 2]
l2=[6, 5, 4]
print(l1 + l2)

l1.extend(l2)
print(l1)

'''
4.
Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista

l1.sort()
print(l1)
l1.remove(0)
print(l1)
'''
'''
5. 
Folosind un if verificati lista generata la ex3 si afisati
Lista este goala
Lista nu este goala
'''
l0=[]
if l1==l0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

'''
6. 
Folositi o functie care sa stearga lista de la ex3
'''
l1.clear()
print(l1)
'''
7. 
Copy paste la ex 5. Verificati inca o data.
Acum ar trebui sa se afiseze ca lista e goala
'''
l0=[]
if l1==l0:
    print('Lista este goala')
else:
    print('Lista nu este goala')
'''
8. 
Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folositi o functie ca sa afisati Elevii (cheile)
'''
dict1 = { 'Ana'  : 8,
          'Gigel': 10,
          'Dorel': 5  }
print(dict1.keys())
'''
9. 
Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie
'''
for key, value in dict1.items():
  print(key, 'a luat nota', value )
'''
10.
Dorel a facut contestatie si a primit 6
Modificati nota lui Dorel in 6
Printati nota dupa modificare
'''
dict1.update({'Dorel': 6})
print(dict1)
'''
11.
Gigel se transfera din clasa
Cautati o functie care sa il stearga
Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati noii elevi
'''
dict1.pop('Gigel')
print(dict1)
dict1.__setitem__('Ionica', 9)
print(dict1)

'''
12.
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt
'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

'''
13.
Folositi un if si verificati daca 
Weekend este un subset al zilelor din sapt
Weekend nu este un subset al zilelor din zile_sapt.'''
if weekend.issubset(zile_sapt)==True:
    print('Weekend este un subset al zilelor din sapt')
else: print('Weekend nu este un subset al zilelor din sapt ')

'''
14. Afisati diferentele dintre aceste 2 seturi
'''
print(zile_sapt.difference(weekend))

'''
15.
Afisati intersectia elementelor din aceste 2 seturi
'''
print(zile_sapt.intersection(weekend))
'''
c. Optionale (may need google)
16.
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea 
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori
Google search hint
“how to check if item is in list python" '''
jucatori=['Andres', 'Ion', 'Carlos', 'Rio', 'Vasi']
schimari_max=3
if 'Andres' in jucatori:
    jucatori.remove('Andres')
if 'Andres' not in jucatori:
    jucatori.append('Albert')
print('A intat Albert, a iesit Andres, mai aveti 2 schimbari')
if 'Mario' not in jucatori:
    print('Nu se poate efectua schimbarea deoarece jucatorul Mario nu e in teren' )
print('mai aveti 2 schimbari')
if 'Carlos' in jucatori:
    jucatori.remove('Carlos')
if 'Carlos' not in jucatori:
    jucatori.append('Crevet')
print('A intat Crevet, a iesit Carlos, mai aveti o schimbare')
if 'Rio' in jucatori:
    jucatori.remove('Rio')
if 'Rio' not in jucatori:
    jucatori.append('Doru')
print('A intrat Doru, a iesit Rio, nu mai aveti nici o schimbare')
