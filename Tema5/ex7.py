'''7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
)'''

def count_upper_lower(str):
    x=y=0
    for litera in str:
        if litera.isupper():
            y += 1
        else:
            x += 1
    return y, x


x= count_upper_lower('AaNA are MeRe')
y =count_upper_lower('AaNA are MeRe')
print(f'Caractere lower: {x} \nCaractere upper: {y}')