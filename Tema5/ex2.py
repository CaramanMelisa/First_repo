# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def tip_nr(numar):
    if numar % 2==0:
        return True
    else:
        return False

print(tip_nr(-9.89))