## belajar menggunakan reduce function
from functools import reduce
# contoh 1
# multiply all number in a list
data = [2, 3, 4, 5, 6, 7]
multiplier = lambda x, y: x*y # mengalikan semua data
x = reduce(multiplier, data)
print(x)
print('\n')


# cara biasa
datx = [2, 3, 4, 5, 6, 7]
jumlah = 1
for i in datx:
    jumlah = jumlah * i

print(jumlah)