from math import*
catetoA = float(input("Digite o primeiro lado do triângulo: "))
catetoB = float(input("Digite o segundo lado do triângulo: "))

def hipotenusa(a, b):
    hipo = sqrt((catetoA**2 + catetoB**2))
    return hipo


print("Hipotenusa: %.2f" % hipotenusa(catetoA, catetoB))