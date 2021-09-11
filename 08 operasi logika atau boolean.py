# operasi logika atau boolean
# not, or, and, XOR

# NOT
print('====NOT====')
a = False
c = not a
print('data a =', a)
print('data c(c = not a) =', c)

# OR
print('====OR====')
a = False
b = False
c = a or b
print(a, 'or', b, '=', c) # akan bernilai True jika salah satu bernilai True
a = False
b = True
c = a or b
print(a, 'or', b, ' =', c)
a = True
b = False
c = a or b
print(a, ' or', b, '=', c)
a = True
b = True
c = a or b
print(a, ' or', b, ' =', c)

# AND
print('====AND====')
a = False
b = False
c = a and b
print(a, 'and', b, '=', c) # akan bernilai True jika dua-duanya True
a = False
b = True
c = a and b
print(a, 'and', b, ' =', c)
a = True
b = False
c = a and b
print(a, ' and', b, '=', c)
a = True
b = True
c = a and b
print(a, ' and', b, ' =', c)

# XOR ^
print('====XOR====')
a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c) # akan bernilai False jika dua-duanya False
a = False
b = True
c = a ^ b
print(a, 'xor', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, ' xor', b, '=', c)
a = True
b = True
c = a ^ b
print(a, ' xor', b, ' =', c)