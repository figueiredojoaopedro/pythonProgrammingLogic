letra = input("Digite a letra desejada: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print ("Essa letra é uma vogal")
elif letra == "y":
    print ("Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.")
else:
    print ("Essa letra é uma consoante.")