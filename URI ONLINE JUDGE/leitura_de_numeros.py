lista_maior = []
lista_menor = []
lista_final = []
entrada = 0

while True:
    entrada = int(input(""))
    if entrada >= 1:
        lista_maior.append(entrada)
    elif entrada < 0:
        lista_menor.append(entrada)
    if entrada == 0:
        break

for s in range(0, len(lista_menor)):
    lista_final.append(lista_menor[s])

for b in range(0, len(lista_maior)):
    lista_final.append(lista_maior[b])

print(lista_final)