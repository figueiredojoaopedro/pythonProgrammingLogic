planeta = str(input("Digite o o nome do planeta desejado: "))
peso = float(input("Digite o peso da pessoa na Terra em kg: "))

def pesoPlanetario (weight, planet):
    if planet == "Mercúrio":
        weight_wished = weight * 0.37
        print("Peso em %s: %.2f" % (planeta, weight_wished))
    elif planet == "Vênus":
        weight_wished = weight * 0.88
        print("Peso em %s: %.2f" % (planeta, weight_wished))
    elif planet == "Marte":
        weight_wished = weight * 0.38
        print("Peso em %s: %.2f" % (planeta, weight_wished))
    elif planet == "Júpiter":
        weight_wished = weight * 2.64
        print("Peso em %s: %.2f" % (planeta, weight_wished))
    elif planet == "Saturno":
        weight_wished = weight * 1.15
        print("Peso em %s: %.2f" % (planeta, weight_wished))
    elif planet == "Urano":
        weight_wished = weight * 1.17
        print("Peso em %s: %.2f" % (planeta, weight_wished))
    elif planet == "Netuno":
        weight_wished = weight * 1.18
        print("Peso em %s: %.2f" % (planeta, weight_wished))

pesoPlanetario(peso, planeta)