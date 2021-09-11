# format string
# contoh generic

# string
nama = "iqram"
format_str = f"hello {nama}"
print(format_str)

# angka
angka = 2005.55
format0 = f"angka = {angka}"
print(format0)

# boolean
boolean = True
format1 = f"boolean = {boolean}"
print(format1)
print("")

# bilangan bulat
bil_bul = 15
format2 = f"bilangan bulat = {bil_bul:d}"
print(format2)

# bilangan dgn ordo ribuan
bil_ribu = 2000000
format3 = f"bilangan jutaan = {bil_ribu:,}"
print(format3)

# bilangan desimal
bil_des = 2005.4123
format4 = f"bilangan desimal = {bil_des:.3f}"
print(format4)

# menampilkan leading zero
bil_des = 2005.4123
format4 = f"bilangan desimal = {bil_des:010.3f}"
print(format4)

# menampilkan angka dgn tanda - atau +
angka1 = -5.23912
angka2 = 4
format_minus = f"bilangan negatif = {angka1:+.2f}"
format_plus = f"bilangan positif = {angka2:+d}"
print(format_minus)
print(format_plus)

# memformat persen
angka3 = 0.045
format_persen = f"bilangan persen = {angka3:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 1000
jumlah = 30
nilai = f"harga akhir = {harga*jumlah:,}"
print(nilai)
print("")

# format angka lain (binary, octal, hexadecimal)
angka = 255
print(angka)
format_binary = f"format binary = {bin(angka)}"
format_octal = f"format octal = {oct(angka)}"
format_hex = f"format hexadecimal = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)