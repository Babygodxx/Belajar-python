def WTF() :
    print(" tired")

def never_quit() :
    print("tired")

def take_a_rest() :
    print("tired")

def stop () :
    print("break")


def show_menu() :
    print("\n")
    print("[1] WTF ")
    print("[2] never quit ")
    print("[3] Take a rest ")
    print("[4] break") 

    menu = int(input("select menu : "))
    print("\n")

    if menu == 1 :
        WTF()
    elif menu == 2 :
        never_quit()
    elif menu == 3 :
     take_a_rest()
    elif menu == 4 :
        stop()

    else :
     print("ANDA TIDAK BOLEH KUAT ANDA LEMAH")

print("=========KULIAH===========")
print("==========MENU==========")
print("\n")
jawab = "y"
while (jawab == "y") :
    show_menu()
    jawab = input("ulang lagi atau tidak (y/n) ?")
    if jawab != "y" :
        break


