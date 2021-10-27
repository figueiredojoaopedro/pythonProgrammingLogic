from random import randint

M10X15 =[]
for num_linha in range(0,10):
    linha = []
    for num_coluna in range(0,15):
        linha.append(randint(0,100))
    M10X15.append(linha)

for line in range(len(M10X15)):
    for column in range(len(M10X15[line])):
        print("%4d" % M10X15[line][column], end=" ")
    print()