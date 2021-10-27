from random import randint, uniform

inteiros = []
reais = []
strings = []
complexos = []
lista = []

for i in range (0,10):
    entry_int = randint(0,1000)
    inteiros.append(entry_int)
print(inteiros)
for j in range (0,15):
    entry_float = uniform(0,1000)
    reais.append(entry_float)
print(reais)
for k in range(0,7):
    entry_string = input("Digite: ")
    strings.append(entry_string)
print(strings)
for l in range(0,5):
    entry_complex = complex(input("Digite um complexo: "))
    complexos.append(entry_complex)
print(complexos)
lista.append(inteiros, reais, strings, complexos, lista)
print(lista)
lista.remove(inteiros, reais, strings, complexos, lista)
print(lista)

for f in range(0,50):
    entry_integer = randint(0,1000)
    lista.append(entry_integer)

print (lista)