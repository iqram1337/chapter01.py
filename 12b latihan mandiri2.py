a = int(input("masukkan nilai awal: "))
b = int(input("masukkan batas nilai: "))
i = a
jumlah = 0
while (i <= b):
    if(i < b):
        print(i, '+', end=' ')
    elif(i == b):
        print(b, '=', end=' ')
        
    jumlah += i
    i += 1

print(jumlah)