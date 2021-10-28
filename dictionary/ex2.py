import random
vezes = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
}
def dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    #returning the sum of both dados
    somatoria = dado1 + dado2
    vezes[somatoria] = vezes[somatoria] + 1
def main():
    soma = 0
    for i in range(0,1000):
        dados()
        soma += 1
    for chave, valor in vezes.items():
        print('%i %i %.2f%%'% (chave, valor, (valor/soma) * 100))
main()