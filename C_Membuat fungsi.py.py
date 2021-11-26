#Fungsi ditandain dengan Def
#penggunaan fungsi berbagai macam seperti
#tanpa parameter
#dengan parameter
##dengan parameter tidak terbatas
#dengan argumen defult
#denganperhitungan geometri
#dengan percabangan


#contoh tanpa parameter
def about() :
    print("copiright by M fiki alimul anam")
    print("Email : fikialimula@gmail.com")

about()

#contoh dengan parameter
def ucapan(input_nama) :
    print("selamat datang", input_nama)
    print("selamat bersenang-senang")

ucapan("fiki")

#dengan parameter tidak terbatas
def Panggil(*nama):
    print("daftar buah sebagai berikut :")
    for buah in nama :
        print("-", buah)

Panggil("apple", "mangga", "jeruk", "srikaya")
print("="*50)
def hargasawit(kg):
    harga = 2200
    hargatotal = kg*harga
    print("ini adalah harga sawit pada bulan ini", harga,"per kg", "jadi total harganya adalah", hargatotal)
   
hargasawit(6)

print("="*20)
def matkul(jam, pelajaran) :
    print("jam kuliah :", jam)
    print("pelarajan nya adalah :", pelajaran)

matkul(jam='10', pelajaran='logika matematika ')

#funsi dengan percabangan
def show_menu():
    print("\n")
    print("-----------menu----------")
    print("[1] show data")
    print("[2] insert data")

    menu = int(input("PILIH MENU"))
    print("\n")

    if menu == 1:
        print("pilih submenu 1")
    if menu == 2 :
        print("pilih submenu 2")

    show_menu()
    

