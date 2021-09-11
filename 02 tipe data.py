# a = 10, a adalah variabel dengan nilai 10 (sepuluh)

# tipe data: angka bilangan bulat (integer)
data_integer = 1
print("data :", data_integer, ", bertipe :", type(data_integer))

print("-------------------------------------------------")

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data: ", data_float, ", bertipe: ", type(data_float))

print("-------------------------------------------------")
# tipe data: kumpulan karakter (string)
data_string = "iqram"
print("data: ", data_string, ", bertipe: ", type(data_string))

print("-------------------------------------------------")
# tipe data: biner true/false (boolean)
data_bool = False # bisa True / False
print("data: ", data_bool, ", bertipe: ", type(data_bool))


## tipe data khusus
print("-------------------------------------------------")
#bilangan kompleks
data_kompleks = complex(5,6) # penulisan matematikanya adalah 5+6i, 6i merupakan bil. imajiner
print("data: ", data_kompleks, ", bertipe: ", type(data_kompleks))

print("-------------------------------------------------")
# tipe data dari bahasa C
from ctypes import c_double # kita bisa import c_char, c_long, dan lain-lain
data_c_dabel = c_double (10.5)
print("data: ", data_c_dabel, ", bertipe: ", type(data_c_dabel))