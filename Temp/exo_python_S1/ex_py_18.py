liste = [1,-6,2,3,-3,5,-12,23,2,12]

print(liste)


def compteurs():
    i = 0
    n = 0
    liste_positif=[]
    count = int(len(liste))
    while i < count :
        if liste[n] > 0 :
            liste_positif.append(liste[n])
        n += 1
        i += 1
    print(liste_positif)


compteurs()