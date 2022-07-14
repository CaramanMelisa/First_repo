'''

ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)

Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)

POLYMORPHISM
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
'''

from abc import abstractmethod

pi = 3.14
class FormaGeometrica:


    @abstractmethod

    def aria(self):
        raise NotImplementedError

    def descriere(self):
        print('Cel mai probabil am colturi')

class Cerc(FormaGeometrica):
    __raza = None
    def __init__(self, raza):
        self.__raza=raza


    def aria(self):
        a= pi * self.__raza**2
        return a
    def descriere(self):
        print('Sunt un CERC')

class Dreptunghi(FormaGeometrica):
    __lungime = None
    __latime = None
    def __init__(self, lungime, latime):
        self.__lungime=lungime
        self.__latime = latime

    def aria(self):
        a = self.__latime * self.__lungime
        return a
    def descriere(self):
        print('Sunt un DREPTUNGHI')

cerc=Cerc(32)
cerc.aria()
print(cerc.aria())

dreptunghi = Dreptunghi(44, 2)
print(dreptunghi.aria())

list = [cerc, dreptunghi]
for i in list:
    i.descriere()
    print(i.aria())
