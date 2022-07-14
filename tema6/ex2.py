'''
2.
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().'''



class  Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f'Dreptungiul are lungimea {self.lungime}, latimea, {self.latime} si culoarea {self.culoare}')

    def aria(self):
        print(f'Arie este: {self.latime * self.lungime}')

    def perimetru(self):
        print(f'Perimetrul este: {2* self.latime + 2 * self.lungime}')

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare



dr1=Dreptunghi(22,4, 'ROSU')
dr1.descriere()
dr1.aria()
dr1.perimetru()
dr1.schimba_culoarea('VERDE')
dr1.descriere()
dr2=Dreptunghi(32,3, 'Alb')
dr2.descriere()
dr2.aria()
dr2.perimetru()
dr2.schimba_culoarea('GALBEN')
dr2.descriere()






