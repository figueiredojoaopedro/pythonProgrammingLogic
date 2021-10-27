from random import randint, uniform

inteiros = []
reais = []
strings = []
complexos = []
completa = []

for i in range(0,10):
    num_int = randint(0,100)
    inteiros.append(num_int)
print(inteiros)

for r in range(0,15):
    num_float = uniform(0,10)
    reais.append(num_float)
print(reais)

for s in range(0,7):
    entrada_string = input("Entre uma string: ")
    strings.append(entrada_string)
print(strings)

for c in range(0,5):
    entrada_complex = input("Entre um complexo")
    complexos.append(entrada_complex)
print(complexos)

completa.append(inteiros)
completa.append(reais)
completa.append(strings)
completa.append(complexos)
print(completa)
completa.remove(inteiros)
completa.remove(reais)
completa.remove(strings)
completa.remove(complexos)
print(completa)

for complete in range(0,50):
    num_compl = randint(0,100)
    completa.append(num_compl)
print(completa)