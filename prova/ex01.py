def compute_bill(lista):
    stock = {
        'banana': 12,
        'pera': 7,
        'morango': 1,
        'caqui': 10
    }
    prices = {
        'banana': 3,
        'pera': 5,
        'morango':7.5,
        'caqui':4
    }
    total = 0
    naoComprado = []
    for x in lista:
        preco = prices[x]

        if stock[x]>1:
            total=total +preco
            stock[x]=stock[x] -2
        else:
            naoComprado.append(x)
        return total,naoComprado

lista_de_compras = ['banana','morango','caqui']

print(3+4)

