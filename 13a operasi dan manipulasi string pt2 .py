# operasi dalam bentuk methods

## mengubah case pada string
test1 = "bro!"
print("normal = " + test1)
test1 = test1.upper()
print("upper = " + test1)   # menjadi upper case
test2 = "hAlO NaMa sAYa IqRaM"
print("normal = " + test2)
test2= test2.lower()
print("lower = " + test2)
print("")

## pengecekan dengan isX method
# pengecekan lower case
test3 = "iqram"
is_lower = test3.islower()
print(test3 + " is lower = " + str(is_lower))
is_upper = test3.isupper()
print(test3 + " is upper = " + str(is_upper))

# isalpha = untuk mengecek semua alfabet
# isalnum = untuk mengecek alfabet dan angka
# isdecimal = untuk mengecek angka saja
# isspace = untuk mengecek spasi, tab, newline \n
# istitle = untuk mengecek semua kata dimulai dengan huruf kapital

judul = "Pengolahan Abu Batubara Sebagai Bahan"
cek1 = judul.istitle()
print(judul + "is title = " + str(cek1))
print("")

# mengecek komponen  starswith() dan endswith()
test0 = "Iqram Haris Fahromi"
cek0 = test0.startswith("Iqram")
print(test0 + " diawali dgn Iqram = " + str(cek0))
cek0 = test0.startswith("iqram")
print(test0 + " diawali dgn iqram = " + str(cek0))
cek0 = test0.endswith("Fahromi")
print(test0 + " diakhri dgn Fahromi = " + str(cek0))
print("")


## penggabungan komponen join() split()
pisah = ['iqram', 'haris', 'fahromi']
gabungan = ', '.join(pisah)
print(gabungan)

pisah1 = "iqram,haris,fahromi"
gabungan1 = pisah1.split(',')
print(gabungan1)
print("")


## alokasi karakter rjust(), ljust(), center()
kanan = "kanan"
kiri = "kiri"
tengah = "tengah"
print('"' + kanan.rjust(10) + '"')
print('"' + kiri.ljust(10) + '"')
print('"' + tengah.center(20, "-") + '"')

# kebalikannya = strip()
print('"' + tengah.strip("-") + '"') # menghilangkan tanda -

