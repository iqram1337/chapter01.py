# operator bitwise, biner, binary

a = 9
b = 5

# bitwise OR |
c = a | b
print("=====OR=====")
print('nilai :', a, ', binary  :', format(a, '08b'))
print('nilai :', b, ', binary  :', format(b, '08b'))
print('------------------------------(|)')
print('nilai :', c, ', binary :', format(c, '08b'))

# bitwise AND &
c = a & b
print("=====AND=====")
print('nilai :', a, ', binary  :', format(a, '08b'))
print('nilai :', b, ', binary  :', format(b, '08b'))
print('------------------------------(&)')
print('nilai :', c, ', binary  :', format(c, '08b'))

# bitwise XOR ^
c = a ^ b
print("=====XOR=====")
print('nilai :', a, ', binary  :', format(a, '08b'))
print('nilai :', b, ', binary  :', format(b, '08b'))
print('------------------------------(^)')
print('nilai :', c, ', binary :', format(c, '08b'))

# bitwise NOT ~
c = ~a
print("=====NOT=====")
print('nilai :', a, ', binary  :', format(a, '08b'))
print('------------------------------(~)')
print('nilai :', c, ', binary:', format(c, '08b'))
print('------------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :', d^e, ', binary:', format(d^e, '08b'))

# shifting << atau >>
print("=====SHIFTING=====")
c = a >> 1
print('nilai :', a, ', binary  :', format(a, '08b'))
print('nilai :', c, ', binary  :', format(c, '08b'), " > 1")
c = a << 2
print('nilai :', c, ', binary :', format(c, '08b'), " < 2")










