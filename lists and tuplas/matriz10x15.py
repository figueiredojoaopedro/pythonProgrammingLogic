from random import randint
matriz = []

for line in range(0,10):
    linha = []
    for coluna in range(0,15):
        elemento = randint(0,100)
        linha.append(elemento)
    matriz.append(linha)

for l in range(0, len(matriz)):
    for c in range(0, len(matriz[l])):
        print("%4d" % matriz[l][c], end=' ')
    print()