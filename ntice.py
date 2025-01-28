##def vytvor(n):
##    z = list(n)
##    print(z)
    
##def iba_int(ntica):
##    n = []
##    for i in ntica:
##        if type(i) == int:
##            (n.append(i))
##    print(tuple(n))

##def stav(z):
##    p = 0
##    for i in z:
##        rozdiel = max(i)-min(i)
##        if rozdiel > 1.5:
##            p += 1
##    print(p)

##import random
##
##def nahodny_datum():
##    den = random.randint(1,31)
##    mesiac = random.randint(1,12)
##
##    print(tuple([den,mesiac]))


def sucet(ntica1,ntica2):
    prva = sum(ntica1)
    druha = sum(ntica2)
    spolu = prva+druha
    print("Prvá ntica:",prva)
    print("Druhá ntica:",druha)
    print("celá ntica:",spolu)
