# operasi yang dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # ini adalah assignment
print("nilai a =",a)

# operator biasa
a += 1
print("nilai a += 1", ",menjadi =", a)
a -= 2
print("nilai a -= 2", ",menjadi =", a)
a *= 5
print("nilai a *= 5", ",menjadi =", a)
a /= 2
print("nilai a /= 2", ",menjadi =", a)

# modulus
b = 10
print("\nnilai b =", b)
b %= 3
print("nilai b %= 3", ",menjadi =", b)

# floor division
b = 10
print("\nnilai b =", b)
b //= 3
print("nilai b //= 3", ",menjadi =", b)

# eksponen
a = 5
print("\nnilai a =", a)
a **= 3
print("nilai a **= 3", ",menjadi =", a)


# operasi bitwise
# OR
c = True
print("\nnilai c =", c)
c |= False
print("nilai c |= False,", "nilai c menjadi =", c)
c = False
print("nilai c =", c)
c |= False
print("nilai c |= False,", "nilai c menjadi =", c)

# AND
c = True
print("\nnilai c =", c)
c &= False
print("nilai c &= False,", "nilai c menjadi =", c)
c = True
print("nilai c =", c)
c &= True
print("nilai c &= True,", "nilai c menjadi =", c)

# XOR
c = True
print("\nnilai c =", c)
c ^= False
print("nilai c ^= False,", "nilai c menjadi =", c)
c = True
print("nilai c =", c)
c ^= True
print("nilai c ^= True,", "nilai c menjadi =", c)

# SHIFTING
d = 0b0100
print("\nnilai d =", format(d,'04b'))
d >>= 2
print("nilai d >>= 2,", "nilai d menjadi =", format(d,'04b'))
d <<= 1
print("nilai d <<= 1,", "nilai d menjadi =", format(d,'04b'))

