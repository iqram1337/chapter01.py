# episode latihan logika dan komparasi
# membuat gabungan area rentang dari angka

# ++++++ 3 ------ 10 ++++++

data_awal = float(input("masukkan angka kurang dari tiga \natau lebih besar dari sepuluh: "))
print("")
# ++++++++ 3 ------------------
# memeriksa angka input kurang dari 3
periksa_data = (data_awal < 3)
print("kurang dari 3 =", periksa_data)

#-------------- 10 +++++++++++
# memeriksa angka input lebih dari 10
periksa_data2 = (data_awal > 10)
print("lebih besar dari 10 =", periksa_data2)

# ++++++ 3 ------ 10 ++++++
# gabungan
output_akhir = (periksa_data or periksa_data2)
print("angka yang anda masukkan =", output_akhir)
print("============================================")


# kasus irisan --------- 3 +++++++++ 10 --------
data_kedua = float(input("masukkan angka lebih besar dari tiga \ndan kurang dari sepuluh: "))
print("")
# memeriksa angka lebih besar dari 3
angka1 = (data_kedua > 3)
print("lebih besar dari 3 =", angka1)

# memeriksa angka input kurang dari 10
angka2 = (data_kedua < 10)
print("kurang dari 10 =", angka2)

# gabungan
outputkedua = (angka1 and angka2)
print("angka yang anda masukkan =", outputkedua)
