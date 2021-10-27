from random import expovariate


def erastotenes(limit):
    p = 2 # as he asked for
    lista = []
    # noting every number till the limit
    for i in range(0,limit):
        if i > 1:
            lista.append(i)
        else:
            lista.append(0)
    for k in range(0,len(lista)):
        for j in range(0,len(lista)):
            if lista[j] % p == 0 and lista[j] != p:
                lista[j] = 0
        p += 1
    return lista