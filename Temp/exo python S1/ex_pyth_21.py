def suite_de_Fibonacci():
    numb = input("J'ai une surprise, entres un chiffre:",)
    n = int(numb)
    x = 1
    suite_f = [1]
    while x <= n :
        x = x * 2
        if x < n :
            suite_f.append(x)
    print("Alors, heureux !", suite_f)



suite_de_Fibonacci()
