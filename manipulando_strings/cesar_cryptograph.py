def criptCesar(p,n):
    # p is equal to the word received and the n variable is like the value of deslocation in the alphabet
    lista = []
    for i in p:
        x = ord(i)
        letra = x + n
        if (x >= 65  and x <= 90):
            if letra < 65:
                letra = 91 - (65 - letra)
            elif letra > 90 and letra < 97:
                letra = 64 + (letra - 90)
        elif (x >= 97  and x <= 122):
            if letra > 90 and letra < 97:
                letra = 123 - (97 - letra)
            elif letra > 122:
                letra = 96 + (letra - 122)
        else:
            letra = x
        lista.append((chr(letra)).upper())
    
    for i in lista:
        print(i, end="")