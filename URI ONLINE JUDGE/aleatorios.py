from random import randrange

maiorNum = 0
att = 0

for i in range(1, 71):
    numero = randrange (1, 101)
    if numero > maiorNum:
        maiorNum = numero
        att += 1

print ("O maior numero gerado foi {0} e a variavel maior numero foi alterada {1}." .format(maiorNum, att))
