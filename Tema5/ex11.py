#11. Functie care primeste o luna din an si returneaza cate zile are acea luna
from calendar import monthrange
nr_days = monthrange(2022, 1)[1]
print(nr_days)