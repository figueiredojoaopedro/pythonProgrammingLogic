# 6 exercise
s = 0
contador = 0
while True:
    numero = int (input ("Digite o numero: "))
    s = s + numero
    contador += 1
    if numero == 0:
        break

media_aritmetica = s / contador
print("soma: %d" % s)
print(media_aritmetica)
print("{0} vezes" .format (contador))