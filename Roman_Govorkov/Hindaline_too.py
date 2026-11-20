# Parandasin kirjavead, tingimused ja lisasin menüü, try/except ning täisnurkse kolmnurga kontrolli.

print("Vali programm:")
print("1 - Kolmnurga kontroll")
print("2 - Hinde arvutamine")
print("3 - Pileti hind")

try:
    valik = int(input("Sisesta valik (1-3) => "))

    if valik == 1:
        print("Kolmnurga kontroll")  # parandasin jutumärgid
        a = float(input("Sisesta 1. külje pikkus => "))  # lisasin float()
        b = float(input("Sisesta 2. külje pikkus => "))  # lisasin sulu )
        c = float(input("Sisesta 3. külje pikkus => "))

        # lisaülesanne: ei tohi olla 0 või negatiivne
        if a <= 0 or b <= 0 or c <= 0:
            print("Vigane külje pikkus")
        elif a + b > c and a + c > b and b + c > a:  # parandasin or -> and ja lisasin kooloni
            print("Kolmnurk on olemas")
            if a == b == c:  # parandasin = -> ==
                print("Kolmnurk on võrdkülgne")
            elif a == b or b == c or a == c:  # parandasin else if -> elif ja lisasin a == c
                print("Kolmnurk on võrdhaarne")
            else:
                print("Kolmnurk on erikülgne")  # lisasin taande (Tab)

            # lisaülesanne: Pythagorase teoreem (täisnurkne kolmnurk)
            if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
                print("Kolmnurk on täisnurkne")
        else:
            print("Sellist kolmnurka ei ole olemas")

    elif valik == 2:
        print("Hinde arvutamine")
        punktid = int(input("Sisesta punktide arv (0-100) => "))
        
        if punktid < 0 or punktid > 100:  # parandasin and -> or
            print("Vigane punktide arv")
        elif punktid >= 90:  # parandasin järjekorra (suuremast väiksemani)
            print("Hinne: 5")
        elif punktid >= 75:
            print("Hinne: 4")
        elif punktid >= 50:
            print("Hinne: 3")
        else:
            print("Hinne: 2")

    elif valik == 3:
        print("Pileti hind")
        vanus = int(input("Sisesta oma vanus => "))
        
        if vanus < 7:
            print("Pilet on tasuta")
        elif (7 <= vanus <= 18) or vanus >= 65:  # parandasin => -> >=
            print("Pileti hind on 3 €")
        else:  # lisasin kooloni ja sulu )
            print("Pileti hind on 6 €")

    else:
        print("Vigane valik")

except:
    print("Vigane sisend!")
