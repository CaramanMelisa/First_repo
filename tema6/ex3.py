'''
3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''

class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul cu numele: {self.nume} si prenumele: {self.prenume} are salariul: {self.salariu}.')
    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.prenume + self.nume}')
    def salariu_lunar(self):
        print(f'Salariul lunar este: {self.salariu}')
    def salariu_anual(self):
        print(f'Salariul anual este: {self.salariu * 12}')

    def marire_salariu(self, procent):
        noul_salariu = self.salariu * (1 + procent/100)
        print(f'Noul salariu este {noul_salariu}')

angajatul1 = Angajat('Mitrică', 'Vali', 6500)
angajatul1.descrie()
angajatul1.nume_complet()
angajatul1.salariu_lunar()
angajatul1.salariu_anual()
angajatul1.marire_salariu(16)
angajatul2 = Angajat('Carin', 'Carmen', 7870)
angajatul2.descrie()
angajatul2.nume_complet()
angajatul2.salariu_lunar()
angajatul2.salariu_anual()
angajatul2.marire_salariu(5)

