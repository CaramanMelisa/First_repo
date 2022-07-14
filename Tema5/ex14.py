#Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        maxim=a
    elif (b >= a) and (b >= c):
        maxim= b
    else:
        maxim = c
    return maxim
print(maximum(3,44,43))