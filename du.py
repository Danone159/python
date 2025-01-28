##z = [3, 5, 25, 4, 7, 49, 35, 12]
##
##def nas_patky(zoz):
##    nas = []
##    for i in zoz:
##        if i % 5 ==0:
##            nas.append(i)
##    print(nas)
##
##nas_patky(z)

i = [3, 5, 25, 4, 7, 49, 35, 12]

def kazde_druhe_cislo(cisla):
    for i in range(0, len(cisla)):
        if i % 2 == 0:
           print(cisla[i])

kazde_druhe_cislo(i)
