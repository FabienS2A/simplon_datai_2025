print("Vous allez entrer 5 entiers")

def cinq_entiers():
    liste_entier = []
    for n in range(5):
        liste_entier.append(input("Entrez un entier :",))
    print(liste_entier)

cinq_entiers()