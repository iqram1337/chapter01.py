# mengecek bilangan bulat
nilaix = int(input("masukkan nilai x: "))


if(nilaix >= 0):
    if(nilaix > 0):
        mod = nilaix % 2
        if(mod == 0):
            print("x adalah bilangan genap positif")
        elif(mod != 0):
            print("x adalah bilangan ganjil positif")
    else:
        print("x adalah bilangan nol")

if(nilaix < 0):
    print("merupakan bilangan negatif")
