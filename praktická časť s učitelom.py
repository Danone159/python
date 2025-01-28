##          Z hodiny zmrzlinár, štatistika, daň

##trzby = []
##
##def pridaj_trzbu():
##    t = int(input("Zadaj trzbu: "))
##    trzby.append(t)
##    print("Už máš spolu",sum(trzby),"€")
##
##def statistika():
##    print("Podnikám už:",len(trzby))
##    print("Sumar tržieb:",sum(trzby),"€")
##    print("Najväčšia tržba:",max(trzby),"€")
##    print("Najmenšia tržba:",min(trzby),"€")
##    print("Priemer trzieb:",round(sum(trzby)/len(trzby),2),"€")
    
##           na vypočítanie obsahu/obvodu kruhy
    
##from re import S
##
##r = float(input("Zadajte polomer:"))
##s = (3.14*r)**2
####o = 2*3.14*r
##print("obsah je:",round(s,2))
##print("obvod je:",round(o,2))

##             premena meny z eur na CZK

##eur = float(input("Zadaj eura:"))
##czk = round(eur*24.33,2)
##
##print ("Za" ,eur,"eur dostaneš" ,czk, "českých korún")

##            na vypočítanie niečo násobenie a následne odčítanie (čokoláda)

##riadky  = float(input("Zadaj počet riadkov:"))
##stĺpce = float(input("Zadaj počet stĺpcov:"))
##kocky = float(input("Koľko kociek si zjedol:"))
##
##zvyšok = (riadky*stĺpce) - kocky
##print ("Ostane ti" ,zvyšok, "kociek čokolady")

##          Vypísanie jedného slova viac krát    

##n = int(input("Zadaj číslo: "))
##s = str(input("Zadaj slovo: "))+" "
##
##for i in range(n):
##    print(s*(i+1))

##          Vypísanie jedného slova v jednom riadku     

##n = int(input("Zadaj číslo: "))
##s = str(input("Zadaj slovo: "))+" "
##
##print(n*s)


##         Vypísanie teplôt náhodne na celý týždeň

##import random
##
##def náhodná_teplota():
##    t = random.randint(-15,15)
##    return t
##
##def teploty_tyzden():
##    for i in range(7):
##        print(náhodná_teplota())
##
##teploty_tyzden()

##          zpriemerovanie čísiel

##def priemer():
##    a = float(input("Zadajte číslo:"))
##    b = float(input("Zadajte číslo:"))
##
##    print((a+b)/2)
##
##priemer()

##         plnoletosť s true ale False

##def je_plnolety():
##    n = int(input("Zadajte Váš vek:"))
##    if n >= 18:
##        return True
##    else:
##        return False
##
##je_plnolety()

##   grfická časť -  vytvorenie bodov podľa toho kde chceme  

##import tkinter
##
##canvas = tkinter.Canvas(width=600, height=450, bg='white')
##canvas.pack()
##
##xx, yy = 0, 0
##
##def klik(event):
##    global xx, yy
##    x, y = event.x, event.y
##    canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')
##    if xx >= 0:
##        canvas.create_line(xx, yy, x, y)
##    xx, yy = x, y
##
##canvas.bind('<Button-1>', klik)

##          výpočet z týždňov na dni hodiny sekundy

##t = int(input("Zadajte počet týždňov: "))
##print("Zadaný počet ťýždňov predstavuje:")
##print("=",t*7,"dní")
##print("=",t*7*24,"hodín")
##print("=",t*7*24*60,"minút")
##print("=",t*7*24*60*60,"sekúnd")

##         vypísanie císiel deliteľné 5 a dopísanie do zozonamu

##z = [3,5,25,4,7,49,35,12,]
##
##
##def nas_patky(zoz):
##    delitelne = []
##    for x in zoz:
##        if x%5 == 0:
##            delitelne.append(x)
##
##        print(delitelne)
##
##nas_patky(z)
##
##while True:
##    i = input("Zadajte hodnotu: ")
##    if i == "vypísať":
##        nas_patky(z)
##    else:
##        z.append(int(i))

##           balík

##def balik():
##    balik = int(input("Zadajte hmotnosť balíka: "))
##    
##    if balik <= 50:
##        print("Zakaznik nemusí zaplatiť nič")
##    elif balik <= 100 and balik > 50:
##        print("Zakaznik zaplatí sumu 0,70 €")
##    elif balik <= 200 and balik > 100:
##        print("Zakaznik zaplatí sumu 1,30 €")
##    else:
##        print("Zakaznik zaplatí sumu 2 €")

##        random do 6

##import random
##z = 1
##while z != 6:
##    z = random.randint(1,6)
##    print("Padlo číslo",z)
##
##print("vyhral si")

##        random deň mesiac

##import random
##
##def nahodny_datum():
##    den = random.randint(1,31)
##    mesiac = random.randint(1,12)
##
##    print(tuple([den,mesiac]))
