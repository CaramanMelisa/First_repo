#Pentru toate clasele,
# creati cel putin 2 obiecte cu valori diferite
# si apelati toate metodele clasei

'''
1.
Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''
#class
pi=2.14
class Cerc:
    pi=2.14
#atribut
    raza= None
    culoare= None

#constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

#metode
    def descrie_cerc(self):
        print(f'Cercul are raza: {self.raza} si culoarea: {self.culoare}')

    def aria(self):
        print(f'Aria este: {pi*self.raza*self.raza}')


    def diametru(self):
        d = 2 * self.raza
        print(f'Diametrul este: {2* self.raza}')

    def circumferinta(self):
        d = 2 * self.raza
        print(f'Circumferinta este: {pi*d}')

cerc1=Cerc(3,'rosu')
cerc1.descrie_cerc()
cerc1.aria()
cerc1.diametru()
cerc1.circumferinta()
print('\n')
cerc2=Cerc(12,'ALB')
cerc2.descrie_cerc()
cerc2.aria()
cerc2.diametru()
cerc2.circumferinta()






