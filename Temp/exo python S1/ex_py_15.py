mot_test = input("Entrez votre si jolie phrase :",)

def palyndrome(a):
    b = a[::-1]
    if a == b :
        print(True)
    else :
        print(False)

palyndrome(mot_test)