liste = ["olive","bonjour","aurevoir","python","avion"]

voyelle = ["a","e","i","o","u"]

print(liste)

def test() :
    i = 0
    mot_voyelle =[]
    count = int(len(liste))
    while i < count :
        if liste[i][0] in voyelle :
             mot_voyelle.append(liste[i])
        i += 1
    print(mot_voyelle)



test()