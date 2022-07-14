'''
13.
Ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!
'''
import random
numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_ghicit is None:
    numar = int(input('Introduceti un numar: '))
    if (numar_secret >numar):
        print('Nr. secret e mai mare')
    elif (numar_secret < numar):
        print('Nr secret e mai mic')
    else:
        print('Felicitari! Ai ghicit!')
        break