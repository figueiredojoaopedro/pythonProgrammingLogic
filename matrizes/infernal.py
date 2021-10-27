loja=[]
prod=[]
preço=[]

for iloja in range(3):
    loja.append(input("Digite o nome da loja: "))
for iprod in range(5):
    prod.append(input("Digite o nome do produto: "))
for iloja in range(3):
    linha=[]
    for iprod in range(5):
        linha.append(int(input("Digite o preco do produto {0} na loja {1}: " .format(iprod, iloja))))
    preço.append(linha)
#########
print("\nLojas:")
for iloja in range(3):
    print(loja[iloja])
print("\nProdutos:")
for iprod in range(5):
    print(prod[iprod])
print("\nPreços:")
for iloja in range(3):
    for iprod in range(5):
        print("{0:3d}".format(preço[iloja][iprod]), end=" ")
    print()

print("\nPreços menores que R$ 50.00:")
for iloja in range(3):
    for iprod in range(5):
        if preço[iloja][iprod] < 50:
            print("Loja: {0}, produto {1} e preço {2}".format(loja[iloja], prod[iprod], preço[iloja][iprod]))
    print()