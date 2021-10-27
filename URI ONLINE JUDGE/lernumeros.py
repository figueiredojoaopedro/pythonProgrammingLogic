'''
quantidade_de_numeros = int(input("Entre com a quantidade de números que serão digitados: "))
maior_numero = 0
sequencia = 1

for i in range (0, quantidade_de_numeros):
    entrada = int(input("{0}º número : " .format(sequencia)))
    if entrada > maior_numero:
        maior_numero = entrada
    sequencia = sequencia + 1

print ("Maior número digitado: {0}" .format(maior_numero))
'''
numeros = int(input("Entre com a quantidade de números que serão digitados: "))

count = 1
maior = int(input("1º número : "))

while count < numeros:
    count += 1
    temp = int(input("%dº número : " % count))
    if temp > maior:
        maior = temp
        
print("Maior número digitado:", maior)