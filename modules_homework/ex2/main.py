import baguioDeErastostenes 

def main():
    limit = int(input('Digite um limite para os números primos: ')) # asking to input the limit of the sequence to count how many cousins numbers there are
    lista = []
    lista = baguioDeErastostenes.erastotenes(limit)
    for i in range(0, len(lista)):
        print(lista[i], end=" ")
    print(0,end='')
main()