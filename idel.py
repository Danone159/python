##def zisti(c1,c2):
##    if c1 > c2:
##        print(c1 ,"je viac ako", c2)
##    elif c1 < c2:
##        print(c1 + "nie je viac ako",c2)
##    elif c1 == c2:
##        print(c1,"je rovnaké ako", c2)
##zisti(10,5)

##z = [5,8,1,-4,3,2,1]

##for i in z:
##    print(" Vypisujem prvok ", i)

##for i in range(len(z)):
##    print(z,[i])

##zoz = [1200,1150,1340,1500,1200,1222,1060,1430]
##
##def kazdy_druhy_odmena(zoz):
##    for i in range(0,len(zoz),2):
##        zoz[i] += 100
##    print(zoz)    
##kazdy_druhy_odmena(zoz)

##recept = ["kuracie mäso",500,"gramov","sójová omáčka",3,"PL","mrkva",3,"ks","kukuričný škrob",2,"PL","zelené fazuľky",3, "struky","vajíčko",2,"ks"]
##
##def kazdy_druhy_odmena(z):
##    print("Na recept potrebujeme",len(z)/3,"ingrediencií:")
##    for i in range(int(len(z)/3)):
##        print("-", z[i*3], z[(i*3)+1], z[(i*3)+2])
##
##
##kazdy_druhy_odmena(recept)

def vypis_recept(z):
    print("na recept potrebujeme",len(z)//3,"ingrediencií")
    for i in range(0,len(z),3):
        print("-",z[i],z[i+1],z[i+2])

vypis_recept(["kuracie mäso",500,"gramov","sójová omáčka",3,
"PL","mrkva",3,"ks","kukuričný škrob",2,"PL","zelené fazuľky", 
3, "struky","vajíčko",2,"ks"])
