matriz = []
linha0 = []
linha1 = []


elemento00 = int(input("Digite o elemento da linha 0 e coluna 0: "))
maior = elemento00
elemento01 = int(input("Digite o elemento da linha 0 e coluna 1: "))
if maior < elemento01:
    maior = elemento01
elemento10 = int(input("Digite o elemento da linha 1 e coluna 0: "))
if maior < elemento10:
    maior = elemento10
elemento11 = int(input("Digite o elemento da linha 1 e coluna 1: "))
if maior < elemento11:
    maior = elemento11

elemento00 *= maior
elemento01 *= maior
elemento10 *= maior
elemento11 *= maior

linha0.append(elemento00)
linha0.append(elemento01)
linha1.append(elemento10)
linha1.append(elemento11)

matriz.append(linha0)
matriz.append(linha1)

print("Matriz resultante: ")

for linha in range(0, len(matriz)):
    for coluna in range(0,len(matriz[linha])):
        print("%3d" % matriz[linha][coluna], end=' ')
    print()
