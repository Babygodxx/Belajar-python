def segi_empat() :
    print("Menghitung luas segi empat")
    panjang = int(input("masukan panjang :"))
    Lebar = int(input("masukan lebar :"))
    Luas = panjang * Lebar
    print("hasilnya adalah : ", Luas)

def segitiga() :
    print("Menghitung Luas segitiga")
    alas = int(input("masukan alas :"))
    tinggi = int(input("masukan tinggi :"))
    Luas = alas*tinggi
    print("hasilnya adalah : ", Luas)

def lingkaran() : 
    print("menghitung luas")
    A = int(input("masukan luas : "))
    r = int(input("masukan jari jari : "))
    L = A * r
    print("hasilnya adalah : ", L)

def show_menu ():
    print("\n")
    print("[1] segi empat ")
    print("[2] segitiga ")
    print("[3] Lingkaran ")
    print("[4] exit")

    menu = int(input("PILIH MENU"))
    print("\n")

    if menu == 1:
        segi_empat()
    elif menu == 2 :
        segitiga()
    elif menu == 3 :
        lingkaran()
    elif menu == 4 :
        exit()
    else:
        print("salah pilih anjing pilih yang bener ")

print("aplikasi perhitungan luas bangun datar")

print("==========MENU==========")
print("\t")
jawab = "y"
while (jawab == "y") :
    show_menu()
    jawab = input("ulang lagi atau tidak (y/n) ?")
    if jawab != "y" :
        break