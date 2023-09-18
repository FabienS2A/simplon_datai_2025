liste = ["bonjour","aurevoir","python","avion"]

voyelle = ["a","e","i","o","u"]

print(liste)

def test() :
    mot_voyelle =[]
    for n in liste :
        if n[0] in voyelle :
            mot_voyelle.append(n)
    print(mot_voyelle)

test()