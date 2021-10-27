number = int(input ("Digite o número desejado: "))

if number > 1:
    if number % 1 == 0 and number % number == 0:
        print("Número primo")
    else:
        print("Número não primo")
else:
    print("Número inválido")
#tem nada certo