matrix = []
l_count = 0
c_count = 0
maiores_q_10 = 0

for i in range(0,4):
    linha =[]
    for j in range(0,2):
        elemento = int(input('Digite o elemento da linha %d e coluna %d: ' % (l_count, c_count)))
        c_count += 1
        linha.append(elemento)
    c_count=0
    l_count+=1
    matrix.append(linha)

print('Matriz original: ')
for linha in range(0,len(matrix)):
    for coluna in range(0, len(matrix[linha])):
        print('%3d' % matrix[linha][coluna], end=' ')
    print()
print()
for linha in range(0,len(matrix)):
    for coluna in range(0,len(matrix[linha])):
        if matrix[linha][coluna] > 10:
            print('%d é maior que 10!' % matrix[linha][coluna])
            maiores_q_10 += 1
            matrix[linha][coluna] = 0
print('No total, %d elementos são maiores que 10!' % maiores_q_10)

print('\nMatriz sem os números maiores que 10:')
for linha in range(0,len(matrix)):
    for coluna in range(0, len(matrix[linha])):
        print('%3d' % matrix[linha][coluna], end=' ')
    print()