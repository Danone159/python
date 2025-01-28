##1.úloha
##from re import S
##
##
##r = float(input("Zadajte polomer:"))
##s = (3.14*r)**2
##o = 2*3.14*r
##print("obsah je:",round(s,2))
##print("obvod je:",round(o,2))

##2.úloha
##eur = float(input("Zadaj eura:"))
##czk = round(eur*24.33,2)
##
##print ("Za" ,eur,"eur dostaneš" ,czk, "českých korún")

##3 úloha
##riadky  = float(input("Zadaj počet riadkov:"))
##stĺpce = float(input("Zadaj počet stĺpcov:"))
##kocky = float(input("Koľko kociek si zjedol:"))

##zvyšok = (riadky*stĺpce) - kocky
##print ("Ostane ti" ,zvyšok, "kociek čokolady")


##n = int(input("Zadaj číslo: "))
##s = str(input("Zadaj slovo: "))+" "
##
##for i in range(n):
##    print(s*(i+1))


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

##def je_plnolety():
##    n = int(input("Zadajte Váš vek:"))
##    if n >= 18:
##        return True
##    else:
##        return False

##print (je_plnolety)

##def priemer():
##    a = float(input("Zadajte číslo:"))
##    b = float(input("Zadajte číslo:"))
##
##    print((a+b)/2)
##
##priemer()
