'''
 1.
Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
'''
#Instrucțiunea if-else este folosită pentru a executa atât partea adevărată, cât și partea falsă a unei anumite condiții.
# Dacă condiția este adevărată,partea if este executat și dacă condiția este falsă, partea else este executat.
'''
2.
Verifica si afiseaza daca x este numar natural sau nu
'''

x=int(input('Introduceti un nr.: '))
if x>=0:
    print('este natural')
else:
    print('nu este natural')

'''
3.
Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
'''
x=int(input('Introduceti un nr.: '))
if x>0:
    print('este pozitiv')
elif x<0:
    print('este negativ')
else:
    print('este neutru')

'''
4. 
Verifica si afiseaza daca x este intre -2 si 13
'''
x=int(input('Introduceti un nr.: '))
if x>-2 and x<13:
    print('x se afla intre -2 si 13')
else:
    print('nu este intre intre 2 si 13')

'''
5. 
Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
'''
x=int(input('Introduceti un nr.: '))
y=int(input('Introduceti un nr.: '))
if x-y < 5:
    print('Diferenta este mai mica decat 5')
else:
    print('nu este mai mica dcat 5')
'''
6. 
Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
'''
x=float(input('Introduceti un nr.: '))
if not(x>5 and x<27):
    print('NU este intre 5 si 27')
else:
    print('este intre 5 si 27')

'''
7.
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
'''
x=int(input('Introduceti un nr.x: '))
y=int(input('Introduceti un nr.y: '))
if x == y:
    print('sunt egale')
elif x > y:
    print('x este mai mare')
else:
    print('y este mai mare')
'''

8. 
X, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
'''
x=int(input('Introduceti un nr.x: '))
y=int(input('Introduceti un nr.y: '))
z=int(input('Introduceti un nr.z: '))
if x == y == z:
    print('triunhi echilateral')
elif x==y or x==z or y==z:
    print('este isoscel')
else:
    print('oarecare')
'''
9. 
Citeste o litera de la tastatura
Verifica si afiseaza daca este vocala sau nu
'''
x=str(input('Introduceti o litera: '))
if x in ('a', 'e', 'i', 'o', 'u'):
    print('Este vocala')
else:
    print('Nu este vocala')
'''
10.
Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
x=int(input('Introduceti un nota: '))
if x>9:
    print('Ai luat nota A')
elif x>8:
    print('Ai luat nota B')
elif x>7:
    print('Ai luat nota C')
elif x>6:
    print('Ai luat nota D')
elif x > 4:
    print('Ai luat nota E')
else:
    print('Ai luat nota F')
'''
11.Verifica daca x are minim 4 cifre (x e int)
(ex: 7895 are 4string.digits == True)'''
x=int(input('Introduceti un nr.x: '))
if len(str(x)) >= 4:
    print('are minim 4 cifre')
else:
    print('nu are minim 4 cifre')
'''
12.
Verifica daca x are exact 6 cifre 
'''
x=int(input('Introduceti un nr.x: '))
if len(str(x))==6:
    print('nr. are 6 cifre')
else:
    print('nu are exact 6 cifre')

'''
13.
Verifica daca x este numar par sau impar
'''
x=int(input('Introduceti un nr.x: '))
if x%2 == 0:
    print('este par')
else:
    print('este impar')
'''
14. x, y, z (int)
Afiseaza care este cel mai mare dintre ele?
'''
x=int(input('Introduceti un nr.x: '))
y=int(input('Introduceti un nr.y: '))
z=int(input('Introduceti un nr.z: '))
if x>=y and x>=z:
    print('x este cel mai mare')
elif y>=x and y>=z:
    print('y este cel mai mare')
else:
    print('z este cel mai mare')

'''
15. 
X, y, z - reprezinta unghiurile unui triunghi
Verifica si afiseaza daca triunghiul este valid sau nu
'''
x=int(input('Introduceti un nr.x: '))
y=int(input('Introduceti un nr.y: '))
z=int(input('Introduceti un nr.z: '))
if x+y+z ==180:
    print('este triunghi')
else:
    print('nu este triunghi')

