



# # 1️. Sisestatakse 15 arvu.
# # Määrata, mitu neist on täisarvud.

# for i in range(15):
#     try:
#         arv=float(input(f"{i+1}. arv: "))
#         if arv.is_integer():
#             print(f"{arv} on täisarv. ")
#     except ValueError:
#             print("Palun sisestage arv.")

# # #while kasutades
# i = 0
# while i < 15:
#     try:
#         arv=float(input(f"{i+1}. arv: "))
#         if arv.is_integer():
#             print(f"{arv} on täisarv. ")
#     except ValueError:
#             print("Palun sisestage arv.")


# # 2.  Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.
# try:
#     A = int(input("Sisesta arv A: "))
#     summa = 0 
#     for i in range(1, A + 1):
#         summa += i
#     print(f"Summa vahemikus 1 kuni {A} on {summa}.")
# except ValueError:
#     print("Palun sisestage täisarv.")
# # 3. Sisestatakse 8 arvu.
# # Leida nende korrutis (ainult positiivsete arvude puhul).
# korrutis = 1
# for i in range(8):
#     try:
#         arv = float(input(f"{i + 1}. arv: "))
#         if arv > 0:
#             korrutis *= arv
#     except ValueError:
#         print("Palun sisestage arv.")
# print(f"Positivsete arvude korrutis on {korrutis}.")


# # 4.  Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.

# for i in range(10,21):
#     print(f"{i}^2 = {i**2}")
# #while 
# i = 10
# while i <= 20:
#     print(f"{i}^2 = {i**2}")
#     i+= 1

# #5.  Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
# # N väärtus sisestatakse klaviatuurilt.
# N = int(input("N: "))
# summa = 0
# i = 0

# while i < N:
#     arv = int(input("Sisesta arv: "))
#     if arv < 0:
#         summa += arv
#     i += 1

# print("Summa:", summa)

# #6. Klaviatuurilt sisestatakse N arvu.
# # Koosta programm, mis määrab sisestatud arvude seast:

# # negatiivsete arvude arvu,

# # positiivsete arvude arvu,

# # nullide arvu.
# # (N väärtus sisestatakse klaviatuurilt.)

# try:
#     N = int(input("Sisesta arvude kogus N: "))
#     negatiivsed = 0
#     posutiivsed = 0 
#     nullid = 0
#     for i in range(N):
#         try:   
#             arv = float(input(f"{i+1}. arv: "))
#             if arv < 0:
#                 negatiivsed +=1
#             elif arv > 0:
#                 positiivsed += 1
#             else: 
#                 nullid += 1
#         except ValueError:
#                 print ("Palun sisestage arv.")
#     print(f"Negatiivsete arvude arv: {negatiivsed}")
#     print(f"Positiivsete arvude arv: {positiivsed}")
#     print(f"Nullide arv: {nullid}")
# except ValueError:
#     print("Palun sisestage täisarv.") 


#Iseseisev töö 5 ülesanned 
while True:
    print("\nTee valik: ")

    print("1. naturaalarvud 100-st kuni 1000-ni.(13.)")
    print("2. Leia arvude 100 kuni 200 summa, mis on 17-ga jaguvad.(22.)")
    print("3. Kirjutage programm, mis väljastab veeruna read spetsialses vormis:(16.)")
    print("4. Antud on naturaalarv N.Leia, mitu naturaalarvu, mis ei ületa N, ei jagu ühegagi arvudest 2, 3 või 5.(25.)")
    print("5. Spongi Bob praeb kotlette 🍔")
    print("0. välju")


    valik=input("Vali tegevus: ")
    if valik == "0":
        break


    elif valik == "1":
        #1.(13.) Leia kõik naturaalarvud 100-st kuni 1000-ni, mis on 7-ga jaguvad.
        # Arvuta ka nende arv ja summa.
        kogus = 0
        summa = 0

        for i in range(100, 1001):
            if i % 7 == 0:
                print(i)
                kogus += 1
                summa += i

        print("7-ga jaguvate arvude arv:", kogus)
        print("Nende arvude summa:", summa)


    elif valik == "2":
#2.(22.)   Leia arvude 100 kuni 200 summa, mis on 17-ga jaguvad.
        kogus = 0
        summa = 0

        for i in range(100, 201):
            if i % 17 == 0:
                print(i)
                kogus += 1
        print("17-ga jaguvate arvude arv:", kogus)
                


    elif valik == "3":
        #3.(16.) Kirjutage programm, mis väljastab veeruna read järgmises vormis:
        # 1 0 0 0 0 0 0 0 0
# 0 2 0 0 0 0 0 0 0
# 0 0 3 0 0 0 0 0 0
# 0 0 0 4 0 0 0 0 0
# 0 0 0 0 5 0 0 0 0
# 0 0 0 0 0 6 0 0 0
# 0 0 0 0 0 0 7 0 0
# 0 0 0 0 0 0 0 8 0
# 0 0 0 0 0 0 0 0 9
        for rida in range(1, 10):
            for veerg in range(1, 10):
                if rida == veerg:
                    print(rida, end=" ")
                else:
                    print(0, end=" ")
            print()


    elif valik == "4":
        #4.(25.) Antud on naturaalarv N. Leia, mitu naturaalarvu, mis ei ületa N, ei jagu ühegagi arvudest 2, 3 või 5.
        n = int(input("Sisesta naturaalarv N: "))
        kogus = 0

        for i in range(1, n + 1):
            if not (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
                kogus += 1

        print("Sobivate arvude kogus:", kogus)
            

# elif valik == "5":

    # else:
    #     print("Vale Valik!")

#EI OLE VEEL VALMIS