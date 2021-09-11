# date and time
import datetime as dt

## contoh
print('CONTOH'.center(40, '='))
tgl_hari_ini = dt.date.today()
print(f"Date: {tgl_hari_ini}")
print(f"Day : {tgl_hari_ini:%A}")
print('\n')

## latihan
print('LATIHAN'.center(40, '='))
print('Masukkan TTL Anda\n')
tanggal = int(input('Tanggal: '))
bulan = int(input('Bulan: '))
tahun = int(input('Tahun: '))

tgl_lahir = dt.date(tahun, bulan, tanggal)
print(tgl_lahir)
print('')

print(f"Hari: {tgl_lahir:%A}")
print(f"Bulan: {tgl_lahir:%B}")
umur_hari = tgl_hari_ini - tgl_lahir
umur_tahun = umur_hari.days // 365
umur_sisa_bulan = (umur_hari.days % 365) // 30
print(f"Umur Hari: {umur_hari.days} hari")
print(f"Umur Tahun: {umur_tahun} tahun, {umur_sisa_bulan} bulan")