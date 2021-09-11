# contoh tanpa menggunakan list comprehension
print('Tanpa List Comprehension'.center(50, '='))
mahasiswa = ['Iqram Haris', 'Hafizh Mualik', 'Kamila Rohma', 'Iqbal Hafiz',
'Dhadat Wicak', 'Muh Riski', 'Haris Elk', 'Indonesia', 'Muh Dimas']

namaI = []
for iq in mahasiswa:
    if iq.startswith('I'):
        namaI.append(iq)
print(namaI)
print('\n')


# contoh dengan menggunakan list comprehension
print('Dengan List Comprehension'.center(50, '='))
mahasiswa = ['Iqram Haris', 'Hafizh Mualik', 'Kamila Rohma', 'Iqbal Hafiz',
'Dhadat Wicak', 'Muh Riski', 'Haris Elk', 'Indonesia', 'Muh Dimas']

namaM = [m for m in mahasiswa if m.startswith('M')]
print(namaM)
print('\n')


# contoh dengan menggunakan list comprehension
print('Dengan List Comprehension'.center(50, '='))
movies = [('Spiderman 3', 1935), ('Avengers The Endgame', 2002), ('Big Game', 1999),
('Avatar of Aang', 1872), ('Tendangan si Madun', 2003), ('James Bond 007', 1998)]

pre2k = [judul for (judul, tahun) in movies if tahun < 2000]
print(pre2k)
print('\n')
