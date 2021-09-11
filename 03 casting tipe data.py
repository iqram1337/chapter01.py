# casting tipe data
# mengubah dari satu tipe ke tipe lainnya
# contoh tipe data: int, float, bool, str

# integer
print("====INTEGER====")
exdata_int = 9
print("data: ", exdata_int, ", bertipe: ", type(exdata_int))

exdata_float = float(exdata_int)
exdata_str = str(exdata_int)
exdata_bool = bool(exdata_int)

print("data: ", exdata_float, ", bertipe: ", type(exdata_float))
print("data: ", exdata_str, ", bertipe: ", type(exdata_str))
print("data: ", exdata_bool, ", bertipe: ", type(exdata_bool)) # akan bernilai False jika bilangan nol, True jika bernilai selain nol


# float
print("====FLOAT====")
exdata_float = 3.8
print("data: ", exdata_float, ", bertipe: ", type(exdata_float))

exdata_int = int(exdata_float)
exdata_str = str(exdata_float)
exdata_bool = bool(exdata_float)

print("data: ", exdata_int, ", bertipe: ", type(exdata_int))
print("data: ", exdata_str, ", bertipe: ", type(exdata_str))
print("data: ", exdata_bool, ", bertipe: ", type(exdata_bool)) # akan bernilai False jika bilangan nol, True jika bernilai selain nol


# str
print("====STRING====")
exdata_str = "10"
print("data: ", exdata_str, ", bertipe: ", type(exdata_str))

exdata_int = int(exdata_str)
exdata_float = float(exdata_str)
exdata_bool = bool(exdata_str)

print("data: ", exdata_int, "bertipe: ", type(exdata_int)) # string harus angka
print("data: ", exdata_float, "bertipe: ", type(exdata_float)) # string harus angka
print("data: ", exdata_bool, "bertipe: ", type(exdata_bool)) # akan False jika string kosong


# boolean
print("====BOOLEAN====")
exdata_bool = True
print("data: ", exdata_bool, ", bertipe: ", type(exdata_bool))

exdata_int = int(exdata_bool)
exdata_float = float(exdata_bool)
exdata_str = str(exdata_bool)

print("data: ", exdata_int, ", bertipe: ", type(exdata_int))
print("data: ", exdata_float, ", bertipe: ", type(exdata_float))
print("data: ", exdata_str, ", bertipe: ", type(exdata_str))