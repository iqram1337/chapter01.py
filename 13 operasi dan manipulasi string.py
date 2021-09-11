# operasi dan manipulasi string

# 1. menyambung string (concatenate)
n_depan = "iqram"
n_tengah = "H"
n_belakang = "aris"
n_lengkap = n_depan + " " + n_tengah + "'" + n_belakang
print(n_lengkap)

# 2. menghitung panjang string
p_str = len(n_lengkap)
print('panjang str "' + n_lengkap +'" = ' + str(p_str))
print("")

# operator untuk string
# mengecek apakah ada komponen char atau string di string
A = "A"
cek = A in n_lengkap
print("ada " + A + " di " + n_lengkap + " = " + str(cek))
a = "a"
cek = a in n_lengkap
print("ada " + a + " di " + n_lengkap + " = " + str(cek))
a = "a"
cek = a not in n_lengkap
print("tidak ada " + a + " di " + n_lengkap + " = " + str(cek))
print("")

# mengulang string
print("wkwk"*5)
print(5*"wkwk")
print("")

# indexing
print(n_lengkap)
print("index ke-0 = " + n_lengkap[0])
print("index ke-1 = " + n_lengkap[1])
print("index ke-(-1) = " + n_lengkap[-1])
print("index ke-(-2) = " + n_lengkap[-2])
print("index ke-[0:3] = " + n_lengkap[0:3])
print("index ke-[0,2,4,6,8,10] = " + n_lengkap[0:12:2])
print("")

# item paling kecil dan paling besar
print("char paling kecil = " + min(n_lengkap))
print("char paling besar = " + max(n_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi = " + str(ascii_code))

data_char = 110
print("char untuk ASCII 110 = " + str(chr(data_char)))
print("")

# operator dalam bentuk method
cont_str = "iqram haris fahromi"
banyak_data = cont_str.count("i")
print("jumlah i di " + '"' + cont_str + '"' + " = ", str(banyak_data))