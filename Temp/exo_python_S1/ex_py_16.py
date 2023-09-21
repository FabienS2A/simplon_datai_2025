entree = input("Entrez votre numéro fétiche :", )

nombre = int(entree)

def bon_num(a):
    while a != 42:
        entree = input("retentez votre chance :",)
        a = int(entree)
    print("Félicitation vous avez trouvé le numéo magique")
   

bon_num(nombre)