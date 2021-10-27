dimensao = int(input("Digite a dimensão dos vetores: "))
vetorA = []
vetorB = []
produto_escalar = 0

print("Digite o vetor 1:")
#storing values at A array
for i in range(0, dimensao):
    A = int(input(""))
    vetorA.append(A)
print("Digite o vetor 2:")
#storing values at B array
for j in range(0, dimensao):
    B = int(input(""))
    vetorB.append(B)
#calculating dot product
for k in range(0, dimensao):
    produto_escalar += (vetorA[k]*vetorB[k])

print(produto_escalar)