# belajar menginput data

data = input("masukkan data: ")
print("data: ", data, ", bertipe: ", type(data)) # akan selalu bertipe string
print("===============================================")

# jika ingin mendapatkan tipe data integer, maka:
angka = int(input("masukkan angka: "))
print("data: ", angka, ", bertipe: ", type(angka))
print("===============================================")

# jika ingin menggunakan boolean, maka:
biner = bool(int(input("masukkan booleannya: ")))
print("data: ", biner, ", bertipe: ", type(biner)) # akan bernilai true apabila menginput data selain dari nol