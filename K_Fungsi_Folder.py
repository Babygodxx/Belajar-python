print("=======SELAMAT DATANG======")

def kuis() :
    bermain = input("apakah anda siap bermain : ")

    if bermain != 'siap' :
        quit()

    else :
        print("silahkan jawab pertanyaan di bawah ")

    nilai = 0

    jawaban1 = input("apa nama ibukota kalimantan timur yang akan di recanakan :")


    if jawaban1.lower()=='balikpapan' :
        print("yeay anda benar sekali ")
        nilai+= 1
    else :
        print("maaf anda salah silahkan coba lagi :(")


    jawaban2 = input("apa nama ibukota jawa barat ?:")

    if jawaban2.lower()=='bandung' :
        print("yeay anda benar sekali ")
        nilai+= 1
    else :
        print("maaf anda salah silahkan coba lagi :(")

    jawaban3 = input("apa nama ibukota jawa timur ? :")

    if jawaban3.lower()=='surabaya' :
        print("yeay anda benar sekali ")
        nilai+= 1
    else :
        print("maaf anda salah silahkan coba lagi :(")

    jawaban4 = input("apa nama ibukota jawa tengah ? :")

    if jawaban4.lower()=='semarang' :
        print("yeay anda benar sekali ")
        nilai+= 1
    else :
        print("maaf anda salah silahkan coba lagi :(")

    print("kamu berhasil menjawab : ",str(nilai),"soal")
    Jumlah = nilai*25
    print("jumlah nilai ",Jumlah)


kuis()


