# ------ 0 ++++++ 5 ------- 8 +++++++ 11 -------

data1 = float(input("masukkan angka 0<x<5 atau 8<x<11: "))
# memeriksa ----- 0 ++++++ 5-------
periksa1 = (data1 > 0)
periksa2 = (data1 < 5)
gabungan1 = (periksa1 and periksa2)
#print(gabungan1)

# memeriksa ------ 8 +++++ 11 -----
periksa3 = (data1 > 8)
periksa4 = (data1 < 11)
gabungan2 = (periksa3 and periksa4)
#print(gabungan2)

# gabungan akhir  ------ 0 ++++++ 5 ------- 8 +++++++ 11 -------
gabungan3 = (gabungan1 or gabungan2)
print("angka yang anda masukkan: ", gabungan3   )