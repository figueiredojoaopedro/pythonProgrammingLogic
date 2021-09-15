numero = int(input("Digite o número desejado: "))
contador = 0
i = 0

while i <= numero or contador < 2:
    i += 1
    x = numero % i
    if x == 0:
        contador += 1

if contador <= 2:
    print("Número primo")
else:
    print("Número não primo")
