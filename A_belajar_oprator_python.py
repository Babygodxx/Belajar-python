#oprator 
#1. oprator aritmatika
#2. oprator perbandingan
#3. oprator penugasan
#4. oprator logika
#5. oprator bitwise
#6. oprator percabangan

#1. oprator aritmatika
c = 0
a = int(input("masukan nilai a : "))
b = int(input("masukan nilai b : "))

c = a + b
print(" a + b = " + str(c))

c = a - b
print(" a - b = " + str(c))

c = a * b
print(" a * b = " + str(c))

c = a / b
print(" a / b = " + str(c))

c = a**b
print(" a**b = " + str(c))

#2. oprator perbandingan
a = int(input("masukan nilai a : "))
b = int(input("masukan nilai b : "))

print("cek persamaan")
if(a==b):
    print("-nilai a sama dengan nilai b")
else :
    print("-nilai a sama dengan nilai b")
print("cek pertidaksamaan")
if(a!=b):
    print("nilai a tidak sama dengan b")
else :
    print("-nilai a  tidak sama dengan nilai b")
print("cek lebih dari")
if(a<b):
    print("nilai a lebih dari besar dari nilai b")
else :
    print("-nilai a lebih besar dari nilai b")
print("cek lebih dari atau sama dengan")
if(a<b):
    print("nilai a lebih dari atau sama dengan nilai b")
else :
    print("nilai a lebih dari atau sama dengan nilai b")


#3. oprator penugasan
a = 25
a += 5
print("hasilnya adlah", a)

a = 25
a -= 5
print("hasilnya adlah", a)

a = 25
a *= 5
print("hasilnya adlah", a)

a = 25
a /= 5
print("hasilnya adlah", a)

a = 25
a %= 5
print("hasilnya adlah", a)



#4. oprator logika
a = True
b = False

print("a = " + str(a))
print("b = " + str(b))
#logika And
c = a and b
print("Logika a dan b "+ str(c))
#logika or
c= a or b
print("logika a dan b", c)
#logika not
c = not a
print("logika a dan b", c)

#5. oprator bitwise
# and
a = 34
b = 45
c = a & b
print("a & b : ", c)

#or
a = 34
b = 45
c = a | b 
print("a | b : ", c)

#xor
a = 34
b = 45
c = a ^ b
print("a ^ b : ", c)

#negasi
a = 34
b = 45
c = ~ a
print("~a : ", c)

#shiff right
a = 34
b = 45
c = a >> b
print("a >> b : ", c)

#shif left
a = 34
b = 45
c = a << b
print("a << b : ", c)


#oprator perbandingan
umur = int(input("masukan umur anda : "))
if umur > 50 :
    print(" kamu sudah lansia")
else:
    print("kamu paruh baya")