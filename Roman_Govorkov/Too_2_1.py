# Ülessanne 1
# a) Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.

# Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.
 # b) Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta:
eesnimi=input("Sisesta eesnimi: ")
if eesnimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    elif eesnimi.islower():
        print("Ära sosista, Juku!")
    vanus=int(input(f"Kui vana on {eesnimi}?"))
    if vanus.isdigit():
            vanus=int(vanus)
            if vanus<6:
                pilet="tasuta pilet"
            elif 6<=vanus<14:
                pilet="Lapsepilet"
            elif 14<=vanus<65:
                pilet="täispilet"
            elif 65<=vanus<=100:
                 pilet="soodus pilet"
            else:
                pilet="tundmatu pilet"
                print(f"{eesnimi} vajab {pilet}.")
    else:
            print("Viga andmega")
else:
    print("Täna kinno ei minda")


# 2. Pinginaabrid
# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. Kui jah, teata kasutajale,
#  kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.

pinginaabrid=["Kiruha", "Romanich]
nimi1=input("Sisesta nimi:")