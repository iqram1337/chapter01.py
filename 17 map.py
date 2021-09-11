## contoh penggunaan map
import math

# contoh 1
def area(r):
    return math.pi*(r**2)

radii = [1, 2, 3, 4, 5]

areas = list(map(area, radii))
print(areas)
print('\n\n')

# contoh 2
temps = [("indonesia", 29), ('inggris', 23), ('cairo', 36), ('jepang', 20)]
c_to_f = lambda data: (data[0], 9/5*(data[1]+32))

ans = list(map(c_to_f, temps))
print(ans)