liste = [1,-6,2,3,-3,5]

print(liste)

def positif_int(liste) :
    liste_positif=[]
    for n in liste :
        if n > 0 :
            liste_positif.append(n)
    print(liste_positif)

positif_int(liste)