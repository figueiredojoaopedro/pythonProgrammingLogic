from random import randint
M = []
somatoria = []
soma = 0

for num_linha in range(20):
    linha = []
    for num_coluna in range(10):
        linha.append(randint(0, 10))
    M.append(linha)

print('Matriz original:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print('%3d' % M[linha][coluna], end=' ')
    print()

print('\nVetor com a somatória de cada linha:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        soma = soma + M[linha][coluna]
    somatoria.append(soma)
print(somatoria)

print('\nmatriz depois da multiplicação:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        M[linha][coluna] = M[linha][coluna] * somatoria[linha]
        print('%5d' % M[linha][coluna], end=' ')
    print()