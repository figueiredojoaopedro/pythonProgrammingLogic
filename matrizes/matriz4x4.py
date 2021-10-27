matriz = []
line = []
vetor = []
odds = 0

for linha in range(0, 4):
    for coluna in range(0,4):
        entrada = int(input("Digite: "))
        line.append(entrada)
        if entrada % 2 != 0:
            odds = odds + entrada
    matriz.append(line)
    vetor.append(odds)

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print("%4d" % matriz[l][c], end=" ")
    print()

print(vetor)


