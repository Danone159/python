##def balik():
##balik = int(input("Zadajte hmotnosť balíka: "))
##    
##if balik <= 50:
##    print("Zakaznik nemusí zaplatiť nič")
##elif balik <= 100 and balik > 50:
##    print("Zakaznik zaplatí sumu 0,70 €")
##elif balik <= 200 and balik > 100:
##    print("Zakaznik zaplatí sumu 1,30 €")
##else:
##    print("Zakaznik zaplatí sumu 2 €")
   

##for n in range(1,11):
##    print(" ")
##    for i in range(1,11):
##        print(i*n,end =" ")
        
##import random
##z = 1
##while z != 6:
##    z = random.randint(1,6)
##    print("Padlo číslo",z)
##
##print("vyhral si")


##def je_plnolety():
##    vek = int(input("Zadajte váš vek: "))
##    if vek < 18:
##        print("False")
##    else:
##        print("True")

##def je_plnolety():
##    vek = int(input("Zadajte váš vek: "))
##    print(vek >= 18)

##def priemer():
##
##    z = int(input("Zadajte prvú hodnotu: "))
##    i = int(input("Zadajte druhú hodnotu: "))
##    zoznam = [(z+i)/2]
##    print(zoznam)

def zisti(c1,c2):
    if c1 > c2:
        print(c1," je viac ako ",c2)
    elif c2 > c1:
        print(c1," nie je viac ako ",c2)
    elif c1 == c2:
        print(c1," je rovnaké ako",c2)
