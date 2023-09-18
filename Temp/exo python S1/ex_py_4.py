a = input("Entrez votre nombre test :",)

b = int(a)

def test_pos():
    if b > 0 :
        print("Ce nombre est positif")
    elif b < 0 :
        print("Ce nombre est negatif")
    else :
        print("Ce nombre est nul")

test_pos()