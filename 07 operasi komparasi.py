# operasi komparasi
# >, <, >=, <=, ==. !=, is, is not

a = 4
b = 2

# lebih dari >
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)
print("=============================")

# tidak sama dengan !=
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = a != 2
print(a, '!=', 2, '=', hasil)
print("=============================")

# 'is' sebagai komparasi object indentity
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x:", x, " id:", hex(id(x)))
print("nilai y:", y, " id:", hex(id(y)))
hasil = x is y
print('x is y =', hasil)
print("=============================")

# 'is not' sebagai komparasi object indentity
x = 5 # ini adalah assignment membuat object
y = 6
print("nilai x:", x, " id:", hex(id(x)))
print("nilai y:", y, " id:", hex(id(y)))
hasil = x is not y
print('x is y =', hasil)