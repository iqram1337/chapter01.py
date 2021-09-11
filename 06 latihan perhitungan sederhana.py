# latihan konversi satuan temperature

# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI SATUAN TEMPERATURE\n")
data_celcius = float(input('masukan suhu (celcius): '))

print("suhu: ", data_celcius, "celcius")

# reamur
data_reamur = ((4/5)*data_celcius)
print("suhu: ", data_reamur, "reamur")

# fahrenheit
data_fahrenheit = ((9/5)*data_celcius)+32
print("suhu: ", data_fahrenheit, "fahrenheit")

# kelvin
data_kelvin = data_celcius + 273
print("suhu: ", data_kelvin, "kelvin")