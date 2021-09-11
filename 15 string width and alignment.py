# width and multiline

# data
dnama = "Iqram Haris"
dumur = 19
dtinggi = 168.2
dsepatu = 42

# string standard
print("Data String".center(21, '='))
data_str = f"nama = {dnama}, umur = {dumur}, tinggi = {dtinggi}, sepatu = {dsepatu}"
print(data_str)
print("")

# string multiline (dgn menggunakan \n (enter / newline))
print("Data String".center(21, '='))
data_str = f"nama = {dnama}, \numur = {dumur}, \ntinggi = {dtinggi}, \nsepatu = {dsepatu}"
print(data_str)
print('')

# string multiline (dgn kutip triplets)
data_str = f"""nama = {dnama}
umur = {dumur}
tinggi = {dtinggi}
sepatu = {dsepatu}
"""
print("Data String".center(21, '='))
print(data_str)

# mengatur lebar
dnama = "Iqram"
dumur = 19
dtinggi = 168.2
dsepatu = 42
data_str = f"""nama   = {dnama}
nama   = {dnama.rjust(8)}
nama   = {dnama:>8}
umur   = {dumur:>8}
tinggi = {dtinggi:>8}
sepatu = {dsepatu:>8}
"""
print("Data String".center(21, '='))
print(data_str)
