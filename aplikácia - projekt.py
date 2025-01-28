produkty = ["mlieko", "jablko", "mrkva", "banán", "cibula", "cesnak", "klobása", "slanina"]
ceny = [0.99, 0.55, 0.50, 0.60, 0.39, 0.45, 2.59, 2.99]
hodnotenie = [0, 3, 2.2, 4.2, 3.6, 0, 4.9, 5]

def info_produkty():
    for i in range(len(produkty)):

        if hodnotenie[i] == 0:
            hod = "Nemá"
        else:
            hod = str(hodnotenie[i])
            
        print("-",produkty[i],"- "+str(ceny[i])+"€ -","Hodnotenie ["+hod+"]")

def pridaj_produkt():

    meno = input("Zadajte meno nového produktu: ")
    print("  *(namiesto desatinej čiarky použite bodku)")
    cena = input("Zadajte cenu nového produktu v eurách: ")
    cena = round(float(cena),2)

    produkty.append(meno.lower())
    ceny.append(cena)
    hodnotenie.append(0)
    print(" - Pridali ste produkt pod názvom",meno+", ktoreho cena je",str(cena)+"€.")

def odstran_produkt():

    meno = input("Zadajte meno produktu, ktorý chcete odstrániť: ")

    if meno in produkty:
        i = produkty.index(meno)
        
        produkty.pop(i)
        ceny.pop(i)
        hodnotenie.pop(i)
        print(" - Produkt bol odstránený.")
    else:
        print(" - Produkt nebol nájdený v databáze.")

def recenzia():
    meno = input("Zadajte meno produktu, ktorému chcete pridať alebo zmeniť hodnotenie: ")
    meno = meno.lower()
    
    if meno in produkty:
        hod = float(input("Zadajte hodnotenie od 0 po 5: "))
        if hod >= 0 and hod <= 5:
            hod = round(hod,1)
            hodnotenie[produkty.index(meno)] = hod
            print(" - Produktu pod menom '"+meno+"' ste zmenili hodnotenie na",str(hod)+".")
    else:
        print(" - Produkt nie je v databáze.")

def top5():
    produk = produkty.copy()
    hodnot = hodnotenie.copy()
    print("- Prvých 5 najlepšíe hodnotených produktov v zozname sú:")
    for i in range(5):
        naj = max(hodnot)
        
        print(i+1,"-",produk[hodnot.index(naj)]," ("+str(naj)+")")
    
        produk.pop(hodnot.index(naj))
        hodnot.pop(hodnot.index(naj))

def zdrazit():
    povod = sum(ceny)
    for i in range(len(ceny)):
        ceny[i] = round(ceny[i] * 1.05, 2) 
    print("- Zdražené všetky produkty o 5%.")
    print("Aktuálne zarobíme o", str(round(sum(ceny) - povod, 2))+"€ viac zo všetkých produktov dokopy.")
    
def zlava():
    vyber = input("Pre zlacnenie každého produktu napíšte 'all', pre zlacnenie špecifického produktu napíšte meno produktu: ")
    if vyber == "all":
        print("- Každému produktu sme zlacnili cenu o 10%.")
        for i in range(len(ceny)):
            ceny[i] = round(ceny[i] * 0.9, 2)
    else:
        if vyber in produkty:
            i = produkty.index(vyber)
            ceny[i] = round(ceny[i] * 0.9, 2)
            print(" - Produktu pod menom '"+vyber+"' sme zlacnili cenu o 10%.")
        else:
            print(" - Produkt nie je v databáze.")

def help():
    print("- - - - - - - - - Zoznam príkazov pre systém produktov obchodu:  - - - - - - - - -")
    print("")
    print(" - info_produkty()   - Vypíše produkty z databázy.")
    print(" - pridaj_produkt()  - Pridá produkt do databázy s hodnotením 0.")
    print(" - odstran_produkt() - Odstráni produkt zo databázy.")
    print(" - recenzia()        - Zmení hodnotenie produktu.")
    print(" - top5()            - Vypíše prvých 5 najlešie hodnotených produktov zo databázy.")
    print(" - zdrazit()         - Zvýši ceny každého produktu o 5%.")
    print(" - zlava()           - Zníži cenu všetkých alebo jedného produktu o 10%")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


print("(príkazom - help() - si pozrieš použitelné príkazy)")
