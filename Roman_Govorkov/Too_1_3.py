# atetime moduli funktsioonid date.today(), strftime(), day, month, year
# calendar moduli monthrange(a,b)[b] kuu päevade arv
# try:
#  ...
# except:


# Ülesanne 1
# Kirjuta programm, mis sind tervitab ja kuvab ekraanile tänane kuupäev moduli datetime 
# kasutades ja date.today() funktsiooni abil.
import calendar
from datetime import *
from calendar import *
from math import pi   #monthrange
tana=date.today()
print(f"Tere! \nTäna on {tana}")
# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(f"Täna on {tana1}")

# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(f"Täna on {tana2}")

# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(f"Täna on {tana3}")

# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(f"Täna on {tana4}")

# Omadused day, month, year kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.
# Arvuta oma vanus aastates, kuudes ja päevades.

print("Täna on", tana.day)
print("päev, kuu number on", tana.month)
print("ja aasta on", tana.year)

kuulõpuni=monthrange(tana.year, tana.month)[1] - tana.day
print("kuu lõpuni on jäänud", kuulõpuni, "päeva.")
aastalõpuni=(date(tana.year, 12, 31) - tana).days
print("Aasta lõpuni on jäänud", aastalõpuni, "päeva")
sünnupäev=date(2010, 10, 4)
vanus=aastalõpuni//365
print("Oled",vanus, "aastat, ")
print((aastalõpuni%365)//30, "kuud ja",)
print((aastalõpuni%365)%30, "päeva vana.")


# Ülesanne 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

print("3 + 8 / (4 - 2) * 4", 3 + 8 / (4 - 2) * 4)
print("3 + 8 / 4 - 2 * 4", 3 + 8 / 4 - 2 * 4)
print("(3 + 8) / 4 - 2 * 4", (3 + 8) / 4 - 2 * 4)

# Ülesanne 3
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.
from math import pi
try:
   R = float(input("R: "))
   print("ruudu pindala", R**2)
   print("Ruudu ümbermõõt:", 4*R)
   print("Ringi pindala:", pi*R**2)
   print("Ringi ümbermõõt", 2*pi*R)

except ValueError:
    print("kiruha vass")

# Ülesanne 4
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides 
# ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa.
# Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.
# Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele. 
# Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), 
# siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
# Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne).
# Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
# Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral
# (näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?
earth_km = 6378

earth_perimeter_m = 2 * pi *(earth_km * 1000)

dmonetki = 0.02575

montki = earth_perimeter_m / dmonetki

print(f"dlina ekvatora: {earth_perimeter_m:,.2f} m")
print(f"2 euro: {montki:,.0f}")

# Ülesanne 5
# Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
# kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll
# kill-koll

# Saab kasutada muutujaid. Kuva iga sõna suure tähega.
a="Kill-Koll"
b="Killadi-koll"
print(a.upper() * 3 + b.upper() + a.upper() * 3 + b.upper() + a.upper() * 3)


# Ülesanne 6
# Koosta programm, mis väljastaks järgmised laulusõnad suurte tähtedega:
# Rong see sõitis tsuhh tsuhh tsuhh,
# piilupart oli rongijuht.
# Rattad tegid rat tat taa,
# rat tat taa ja tat tat taa.
# Aga seal rongi peal,
# kas sa tead, kes olid seal?

# Rong see sõitis tuut tuut tuut,
# piilupart oli rongijuht.
# Rattad tegid kill koll koll,
# kill koll koll ja kill koll kill.



# ....Sisend, väljund, tingimus....

print("""RONG SEE SÕITIS TSUHH TSUHH TSUHH,
PIILUPART OLI RONGIJUHT.
RATTAD TEGID RAT TAT TAA,
RAT TAT TAA JA TAT TAT TAA.
AGA SEAL RONGI PEAL,
KAS SA TEAD, KES OLID SEAL?

RONG SEE SÕITIS TUUT TUUT TUUT,
PIILUPART OLI RONGIJUHT.
RATTAD TEGID KILL KOLL KOLL,
KILL KOLL KOLL JA KILL KOLL KILL.""")



# Ülesanne 7
# Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku
# ümbermõõdu ja pindala.

a = float(input("Sisesta esimene külg: "))
b = float(input("Sisesta teine külg: "))

umbermoot = 2 * (a + b)
pindala = a * b

print("Ümbermõõt:", umbermoot)
print("Pindala:", pindala)

# Ülesanne 8
# Kütusekulu arvutamine

#     Kasutaja sisestab tangitud kütuse liitrid
#     Kasutaja sisestab läbitud kilomeetrid
#     Programm leiab kütusekulu 100km kohta keskmiselt


liitrid = float(input("Mitu liitrit kütust tankisid? "))
km = float(input("Mitu kilomeetrit sõitsid? "))

kulu = liitrid / km * 100

print("Kütusekulu 100 km kohta:", round(kulu, 2), "liitrit")


# Ülesanne 9
# Rulluisutajad

#     Rulluisutaja keskmine kiirus on 29,9km/h
#     Kui kaugele jõuab M minutiga


kiirus = 29.9

minutid = float(input("Mitu minutit sõidad? "))

teepikkus = kiirus * minutid / 60

print("Läbitud teepikkus:", round(teepikkus, 2), "km")


# Ülesanne 10
# Ajateisendus

#     Kasutaja sisestab aja minutites
#     Sinu valem leiab ja väljastab tunnid ja minutid
#     Näiteks: sisestus 72, vastus 1:12


minutid = int(input("Sisesta aeg minutites: "))

tunnid = minutid // 60
minutid_jaak = minutid % 60

print(tunnid, ":", str(minutid_jaak).zfill(2), sep="")