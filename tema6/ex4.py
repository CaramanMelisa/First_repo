'''
4.
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''
class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are contul {self.iban} suma de {self.sold}')

    def debitare_cont(self, suma):
        self.sold -= suma
        print(f'Noua suma este: {self.sold} ')

    def creditare_cont(self, suma):
        self.sold += suma
        print(f'Suma este {self.sold}')

cont1= Cont('RO7876M77', 'Andreea Serah', 450000)
cont1.afisare_sold()
cont1.debitare_cont(1000)
cont1.creditare_cont(87676)
print('\n')
cont2= Cont('RO7638RF77', 'Carla Dan', 32100)
cont2.afisare_sold()
cont2.debitare_cont(1320)
cont2.creditare_cont(9006)