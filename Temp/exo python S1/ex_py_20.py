mot = input("Entrez votre mot :")

def test_len_while():
    while len(mot) >= 5 :
        print("Votre mot est long. Bravo !! il contient plus de 5 caractères !!!")
        break

test_len_while()