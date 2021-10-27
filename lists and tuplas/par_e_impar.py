lista = []
lista_par=[]
lista_impar=[]
x = 20

for i in range(0,x):
    entrada = int(input(""))
    lista.append(entrada)
    if entrada % 2 == 0:
        lista_par.append(entrada)
    else:
        lista_impar.append(entrada)

for j in range(0, len(lista)):
    print(lista[j], end=" ")
for k in range(0, len(lista_par)):
    print(lista_par[k], end = " ")
for l in range(0, len(lista_impar)):
    print(lista_par[l], end = " ")
