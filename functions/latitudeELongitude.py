from math import*

latitudeA = radians(float (input("Digite a latitude A: ")))
longitudeA = radians(float (input("Digite a longitude A: ")))
latitudeB =  radians(float (input("Digite a latitude B: ")))
longitudeB = radians(float (input("Digite a longitude B: ")))

def distancia (latitude1, longitude1, latitude2, longitude2):
    dist=6371.01*acos(sin(latitude1)*sin(latitude2)+cos(latitude1)*cos(latitude2)*cos(longitude1-longitude2))
    return dist

print("A distância é %.2fkm." % distancia(latitudeA, longitudeA, latitudeB, longitudeB))