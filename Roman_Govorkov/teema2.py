#   Lihtne If lause
#   2.3   if…else
# try:
#     x = int(input("Sisesta arv: "))
#     if x > 0:
#         print("Positiivne arv")
#         print("See rida on ka if-i sees")
#     print("See rida täidetakse alati")
# except ValueError:
#     print("Valed andmed")
# #if...else lause
# #of tingimus
# #   tegevus_True
# # else: 
# #   tegevus_False


# try:
#     x = int(input("Sisesta arv: "))
#     if x == 1:
#         print("Õige")
#     else:
#         print("Vale")
# except ValueError:
#     print("Valed andmed")



#     vastus = input("Kas soovid jätkata? (jah/ei) ")
# if vastus.lower() == "jah":
#     print("Jätkame!")
# else:
#     print("Head aega!")

#     #   2.4   if…elif…else
#     x = int(input("Sisesta arv -5 kuni 5: "))
# if x < -5:
#     print("Vähe")
# elif -5 <= x <= 5:
#     print("OK")
# else:
#     print("Palju")


#     summa = float(input("Ostusumma: "))
# if summa > 2000:
#     print("Allahindlus 20%")
# elif summa > 1000:
#     print("Allahindlus 10%")
# else:
#     print("Allahindlust pole")





#     vanus = int(input("Vanus: "))
#     if vanus >= 18:
#         juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
#     if juhiluba.lower() == "jah":
#         print("Võid autot juhtida.")
#     else:
#          print("Oled autojuhtimiseks liiga noor.")
# except ValueError:
#         print("Valde andmed. Sisesta arv")

try:
    nimi = input("Sisesta nimi")
    if nimi.isalpha():
        print("Nimi sobib")
        vanus = int(input("Vanus: "))
        if vanus >= 18:
            juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
            if juhiluba.lower() == "jah":
                print("Võid au  t juhtida.")
            else:
                print("Kõigepealt tee juhiload.")
        else:
           print("Oled autojuhtimiseks liiga noor.")
    else:
        print("Nimes tohib olla ainult tähti!")
except ValueError:
    print("Valed andmed. Sisesta arv")

    #<3jjhn
