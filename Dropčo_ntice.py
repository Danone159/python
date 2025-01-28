z = [3,5,25,4,7,49,35,12]

def nas_patky(zoz):
    delitelne = []
    for x in zoz:
        if x%5 == 0:
            delitelne.append(x)

        print(delitelne)

nas_patky(z)
