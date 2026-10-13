#siia kirjutame mis moodulid tahame importida ja hiljem kasutame
print("Tere tulemast!") #kommentaar
print("Esimene programm,mis on kirjatud Pythonis") #sep=" " ,end="\n" väikimsu väärtus 
# #muutujad
# kursus=2 #int
# print("Ma õpin",1,".kursusel") #sep=" " ,end="\n"
# print("Ma õpin",kursus,".kurussel",sep="***",end=". ")
# kursus=int(input("Aga sina?"))
# print("Tore! Sa õpid",kursus,".kursusel. Aga järgmisel aastal",kursus+1,"kursusel")
# nimi = input("Mis on sinu nimi? ")
# print("Tere,", nimi)
# print(nimi,"õpib",kursus,", kurussel")

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a + b)
#Pohioperatsioonid: + - / // % **
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a - b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a / b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a // b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a % b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a * b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a ** b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"+",b,"=", a + b) #liitmine
print(a,"-",b,"=", a - b) #lahutamine
print(a,"*",b,"=", a + b) #korrtamine
print(a,"/",b,"=", a + b) #jagamine
print(a,"//",b,"=", a + b) #jagamise täisarvuline osa
print(a,"%",b,"=", a + b) #jagamisjääk
print(a,"**",b,"=", a + b) #astendamine

nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

#f-sõne kasutamine
hind = 19.9
kogus = 3
print(f"Kokku: {hind * kogus:.2f} eurot")#ühe kümnendkohaga

#stringide ühendamune ja korratamine
print("Tere" + " " + "päevast")
print("-" * 20)
vanus = 17
print("Vanus: " + str(vanus))

import math

#math mooduki kasutamine
print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))

