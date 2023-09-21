liste = ["bonjour","merci","aurevoir","bien","Cocorico"]

def len_list():
    a = int(len(liste))
    liste_len = []
    for n in range(a) :
        liste_len.append(len(liste[n]))
    print(liste_len)

len_list()