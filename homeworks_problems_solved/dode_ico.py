from math import*

poligono = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
aresta = float(input ("Digite o valor da aresta a em metros: "))

if poligono == "dodecaedro":
    volume = ((15 + 7 * sqrt(5)) / 4) * aresta**3
    print("O volume de um dodecaedro regular com %.2f de aresta é: %.2f" % (aresta, volume))
if poligono == "icosaedro":
    volume = ((3 + sqrt(5)) * 5 / 12) * aresta**3
    print ("O volume de um icosaedro regular com %.2f de aresta é: %.2f" % (aresta, volume))