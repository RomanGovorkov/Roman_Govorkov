# 1️. Sisestatakse 15 arvu.
# Määrata, mitu neist on täisarvud.

for i in range(15):
    try:
        arv=float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            print(f"{arv} on täisarv. ")
    except ValueError:
            print("Palun sisestage arv.")

# #while kasutades
i = 0
while i < 15:
    try:
        arv=float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            print(f"{arv} on täisarv. ")
    except ValueError:
            print("Palun sisestage arv.")


# 2.  Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.
try:
    A = int(input("Sisesta arv A: "))
    summa = 0 
    for i in range(1, A + 1):
        summa += i
    print(f"Summa vahemikus 1 kuni {A} on {summa}.")
except ValueError:
    print("Palun sisestage täisarv.")
# 3. Sisestatakse 8 arvu.
# Leida nende korrutis (ainult positiivsete arvude puhul).
korrutis = 1
for i in range(8):
    try:
        arv = float(input(f"{i + 1}. arv: "))
        if arv > 0:
            korrutis *= arv
    except ValueError:
        print("Palun sisestage arv.")
print(f"Positivsete arvude korrutis on {korrutis}.")


# 4.  Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.

for i in range(10,21):
    print(f"{i}^2 = {i**2}")
#while 
i = 10
while i <= 20:
    print(f"{i}^2 = {i**2}")
    i+= 1

#5.  Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
# N väärtus sisestatakse klaviatuurilt.
N = int(input("N: "))
summa = 0
i = 0

while i < N:
    arv = int(input("Sisesta arv: "))
    if arv < 0:
        summa += arv
    i += 1

print("Summa:", summa)

#6. Klaviatuurilt sisestatakse N arvu.
# Koosta programm, mis määrab sisestatud arvude seast:

# negatiivsete arvude arvu,

# positiivsete arvude arvu,

# nullide arvu.
# (N väärtus sisestatakse klaviatuurilt.)

try:
    N = int(input("Sisesta arvude kogus N: "))
    negatiivsed = 0
    posutiivsed = 0 
    nullid = 0
    for i in range(N):
        try:   
            arv = float(input(f"{i+1}. arv: "))
            if arv < 0:
                negatiivsed +=1
            elif arv > 0:
                positiivsed += 1
            else: 
                nullid += 1
        except ValueError:
                print ("Palun sisestage arv.")
    print(f"Negatiivsete arvude arv: {negatiivsed}")
    print(f"Positiivsete arvude arv: {positiivsed}")
    print(f"Nullide arv: {nullid}")
except ValueError:
    print("Palun sisestage täisarv.") 
