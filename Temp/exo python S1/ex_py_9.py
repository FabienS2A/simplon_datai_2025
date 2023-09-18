liste_entier = [1,2,3,4,5,6,7,8,9]

def pair_numb() :
    liste_pair = []
    for n in liste_entier :
        if (n % 2) == 0 :
            liste_pair.append(n)
    print(liste_pair)

pair_numb()