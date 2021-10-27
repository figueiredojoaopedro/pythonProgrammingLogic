amostras = []
desvio_padrao = 0
media = 0
somatoria = 0
n = 0
x = 0

x = int(input("Qual o tamanho da lista: "))

#input of the sample
print("Digite os valores: ")
for i in range(0,x):
    entrada = int(input(""))
    amostras.append(entrada)
    n += 1 #increase the size of the list

#media is equal to all of the values of the sample:
for j in range(0,len(amostras)):
    media += amostras[j]
media = media/n
float(media)
#standard deviation equals the sum of the difference from the mean and each sample value squared
for k in range(0,len(amostras)):
    desvio_padrao += (amostras[k] - media)*(amostras[k] - media)
desvio_padrao = (desvio_padrao/n)**0.5
float(desvio_padrao)

print("Média = {0:.2f} e Desvio = {1:.4f}" .format(media, desvio_padrao ))