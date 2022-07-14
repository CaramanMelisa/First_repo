'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive'''
def pos(lst):
    return [x for x in lst if x > 0] or None

print(pos([-9, 2, 3]))
