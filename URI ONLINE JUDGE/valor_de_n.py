n = int(input("Digite o número desejado: "))
e = 1
contador = 1
i = 0

while i < n:
    i += 1
    e = e + (1 / contador)
    contador += 1

print("%.3f" % e)