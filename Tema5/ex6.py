#6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
#și Talse dacă nu găsește.
str='Am o casuta galbena'
def se_gaseste(x):
    if x in str:
        return True
    else:
        return False
print(se_gaseste(' gal'))