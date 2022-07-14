# 1. O variabila este un spatiu din memorie care inmagazineaza valori.
#2.
book = 'The rain'
nr = 23
rest = 43.423
is_sunny = False
#3.
print(type(book))
print(type(nr))
print(type(rest))
print(type(is_sunny), '\n')
#4
rest=round(rest)
print(type(rest))
#5.
print(f'I am reading the book: {book}. \nMy number is {nr}. \nI have {rest} dollars. \nIs it sunny? {is_sunny}\n')
#6.

numele = 'Budai-Caraman'
prenumele='Melisa'
print(f'Numele complet are {len(numele+prenumele)}\n')
#7.
lungimea =5
latimea = 2
print(f'Aria dreptunghiului este: {latimea * lungimea}')
#8.
string = 'Coral is either the stupidest animal or the smartest rock'
x = 7
print(string[:-x])
#9.
print(string[0:5], string[-5::])
#10.
print(string.count(" the"))
#11.
print(string.replace('the' , 'THE'))
#12.
r='rock'
print(string.rstrip(r))
#13.
input=input('Introduce un cuvant: ')
assert input[0] == input[input.rindex(input)]
print('Primul e egal cu ultimul')
#14.
str='0123456789'
print(str[::2])
print(str[1::2])
#15.
assert str.isnumeric()
print('Yes')
#16
l='lac'
def get_middle(l):
    if len(l)%2==0:
        i = int(len(l)/2)-1
        return l[i]+l[i+1]
    else:
        return l[int(len(l)/2)]
#17.
txt='ana'
assert txt == txt[::-1]



