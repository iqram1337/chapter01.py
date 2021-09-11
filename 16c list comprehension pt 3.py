## scalar multipication

# contoh salah
print('contoh salah'.center(60, '='))
v = [2, -3, 1]
print(v)
x = 4*v
print(x)
print('\n')

# contoh benar
print('contoh benar'.center(60, '='))
a = [2, -3, 1]
print(a)
ans = [4*i for i in a]
print(ans)
print('\n\n')



## cartesian product
print('contoh benar'.center(60, '='))
# example: 
# A = {1, 3}
# B = {x, y}
# A X B = {(1,x), (1,y), (3,x), (3,y)}

vekA = [1, 3, 5]
vekB = [2, 4, 6]
print(vekA)
print(vekB)
print('vek A (x) Vek B')
vekC = [(a, b) for a in vekA for b in vekB]
print(vekC)