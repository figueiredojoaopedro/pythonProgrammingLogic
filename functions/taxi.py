tarifa_basica = 10.00
constante = 0.5
kilometros = int (input ("Digite a quantidade de quilômetros: "))

def preco_corrida (km):
    precoTotal = tarifa_basica + (constante * ((km*1000) / 125))
    return precoTotal

print("Tarifa %.2f" % preco_corrida(kilometros))