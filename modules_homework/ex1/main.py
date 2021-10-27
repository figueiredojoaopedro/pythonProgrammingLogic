import criaPlaca
def main():
    n = criaPlaca.geraNumero()
    l = criaPlaca.geraLetra()
    placa = criaPlaca.montaPlaca(n, l)
    print('Placa =', end=' ')
    for i in placa:
        print(i, end='')

main()