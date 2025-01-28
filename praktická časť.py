trzby = []

def pridaj_trzbu(trzba):
    trzby.append(trzba)
    print("Úspešne ste pridali tržbu vo výške "+str(trzba)+"€! Spolu ste za sezónu zarobili "+str(sum(trzby)),"€")

def statistika():
    print("Počet dní:",len(trzby))
    print("Sumar tržieb:",sum(trzby),"€")
    print("Najväčšia tržba:",max(trzby),"€")
    print("Najmenšia tržba:",min(trzby),"€")
    print("Priemer trzieb:",round(sum(trzby)/len(trzby),2),"€")

def dan():
    print("Daň ktorú musíš odviesť je",sum(trzby)*0.2,"€")
