#List adalah struktur data python yang mampu menyimpan lebih dari satu data
Buah = ["mangga", "durian", "apel", "langsat"]
print (Buah[1])

#contoh lain
print("isi nama ke - 3 adalah :{}".format(Buah[3]))
print("semua teman : ada{}orang".format(len(Buah)))
for tanaman in Buah :
    print(tanaman)
print(50*"=")
#mengganti list
buah = ["anngur","langsat","kelapa"]
buah[2] = "kelapa"
print(buah[2])