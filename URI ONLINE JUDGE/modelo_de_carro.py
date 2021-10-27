modelo_de_carros = []
consumo = []
entrada_modelo = 0
entrada_consumo = 0
mais_eficiente = 0
k = 0

# loop to store all the car's models
for i in range(0, 5):
    entrada_modelo = input("")
    modelo_de_carros.append(entrada_modelo)
# loop to store five times all the consume of teh cars
for j in range(0, len(modelo_de_carros)):
    entrada_consumo = int(input(""))
    consumo.append(entrada_consumo)
    # now, with the lenght function i think i can the
    # index of the array and then show up which
    # one is the most economical car.
    if mais_eficiente < entrada_consumo:
        mais_eficiente = entrada_consumo
        carro_mais_eficiente = modelo_de_carros[j]

print(carro_mais_eficiente)
#KM/L = 5 -> MIL = 1000/5
for k in range(0, len(consumo)):
    mil = 1000/consumo[k] 
    print("%.0f"%mil)

