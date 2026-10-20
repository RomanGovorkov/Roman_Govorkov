from math import * #pi, sqrt
from random import * #randint (a,b) juhusluk täisarv a ja b vahel
#  Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
#  Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
#  Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
#  “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
# #Ülesanne1
# print("Tere, Maailm")
# nimi = input("Mis sinu nimin on?")
# print("Tere, maailm! Tervitan sind",nimi)
# try:
#     vanus=int(input("Kuivana sa oled?"))
#     print("Tere,Maailm!Tervitan sind",nimi,"!Sa oled",vanus,"aastat vana.")
# except ValueError:
#     print("See ei olnud täisarv!")

# # Ülessane2
# # Mis tüüpi on järgnevad muutujad:

# # a) vanus = 18
# # b) eesnimi = "Jaak"
# # c) pikkus = 16.5
# # d) kas_käib_koolis = True
# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis=True
# print("vanus:", vanus, "tüüp:", type(vanus))
# print("eesnimi:", eesnimi, "tüüp:", type(eesnimi))
# print("pikkus:", pikkus, "tüüp:", type(pikkus))
# print("kas_käib_koolis:", kas_käib_koolis, "tüüp:", type(kas_käib_koolis))

#Ülessanne3
# В вашем коде запишите количество конфет на столе в переменную (количество конфет случайное). Затем отобразите количество конфет в переменной на экране с помощью команды print().
# Запросите у пользователя, сколько конфет он хочет убрать со стола. Удалите желаемое количество конфет из количества конфет на столе и отобразите количество конфет на экране.

# from random import * #randint(a,b) juhuslik täisarv a ja b vahel
# kommide_arv =randint(1,1000) #1-100 vahel juhuslik täisarv  от одного до ста (рандом)
# print("Laual on", kommide_arv, "kommi.")
# try:
#     b=int(input("Mitu komi soovid laualt ära võtta?"))
#     kommide_arv-= b #kommidearv vähened b võrra
#     print("Laual on nüüd", kommide_arv, "kommi.")
# except :ValueError
#     print("Palun sisesta kommid numbruna.")


#Ülessanne4
# Расчет диаметра дерева
# # Напишите программу, которая запрашивает у пользователя окружность дерева, а затем сообщает его диаметр.
# ümbermõõt=float(input("Sisesta puu ümbermõõt"))

# läbimõõt=ümbermõõt/pi
# print("Puu läbimõõt on:", läbimõõt)

#Ülesanne5
# Вычислите длину диагонали прямоугольного участка земли размерами N м х M м, используя командную строку Python. Запросите у пользователя значения N и M.
 # N = float(input("Sisesta maatüki pikkus (N): "))
 # M = float(input("Sisesta maatüki pikkus (M): "))
 # diagonaal = sqrt(N**2 + M**2) #** astendamine
 # print("Ristkülikukujulise maatüki diagonaal on:", round(diagonaal,2))
 #round()ümardab kahe kümnendkohani

#Ülesanne6
#Найдите логическую ошибку в следующем примере программы:
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg
# print("Sinu kiirus oli " + str(kiirus) + " km/h")

#Ülesanne7
# arv1 = int(input("Sisesta esimene täisarv: "))
# arv2 = int(input("Sisesta teine täisarv: "))
# arv3 = int(input("Sisesta kolmas täisarv: "))
# arv4 = int(input("Sisesta neljas täisarv: "))
# arv5 = int(input("Sisesta viies täisarv: "))
# summa = arv1 + arv2 + arv3 + arv4 + arv5
# jagaja=int(input("Sisesta arv, millega jagada"))
# tulemus = summa/jagaja
# print("Tulemus:", tulemus)  #tulemus=3.75
# print("Täisarvuline osa:", int(tulemus))
# #int(3.75)=3 teine variant täisosa leidmiseks on kasutada // jagamist: summa//jagaja
# print("Jääk:",summa % jagaja)

#Ülesanne 8
# Joonista samasugune konn
#    @..@
#    (----)
#   ( \__/ )
# ^^ "" ^^  
# print("    @..@")
# print("   (----)")
# print("  ( \__/ )")
# print("   ^^ "" ^^")

#Ülesanne 9
# Давайте вычислим периметр треугольника. Создадим три целочисленные переменные a, b, c.
#  Используем формулу для вычисления периметра треугольника (P = a + b + c).

# a = float(input("Sisesta esimene täisarv: "))
# b = float(input("Sisesta teine täisarv: "))
# c = float(input("Sisesta kolmas täisarv: "))
# P =a + b + c
# print("ümbermõõt on", P)

#Ülesanne 10
# Пицца
# Вы и ваши друзья (например, группа P) заказали большую пиццу, которая стоит 12,90 евро.
# Вы оставляете официанту чаевые в размере 10%.
# Создайте программу, которая вычисляет, сколько должен заплатить каждый человек.

# from random import * #randint (a,b)
# sõbrad = randint(1,10)
# pitsa_hind = 12.90
# jootraha = pitsa_hind * 0.10
# kokku = pitsa_hind + jootraha

#Ülesanne 11
